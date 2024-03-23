from nba_api.live.nba.endpoints import scoreboard
from datetime import datetime
import time
from delivery_tools import Delivery
import pandas as pd
import os as os

# If the criteria has been met, the home team's name will be placed here.
# This will stop the message being sent every 30 seconds.
games_acknowledged = []

# Gets the current time.
start_time = int(time.time())

# Adds 7 hours (from 6 PM to 2 AM) to current time.
end_time = start_time + 28800

# Loop that runs between between 6PM to 2AM
while int(time.time()) < end_time:

    # Gets stats of every game happening today.
    games = scoreboard.ScoreBoard()

    # Turns data into dictionary.
    dict = games.get_dict()

    # Gets just the game stats.
    all_games = dict['scoreboard']['games']

    # For all games happening today.
    for game in all_games:

        # Gets the home team name and score.
        home_team_name = game['homeTeam']['teamName']
        home_team_score = game['homeTeam']['score']

        # Gets the away team name and score.
        away_team_name = game['awayTeam']['teamName']
        away_team_score = game['awayTeam']['score']

        # If it's the 4th quarter and the team is not in the 'do not send' list.
        if 'Q4 ' in game['gameStatusText'] and home_team_name not in games_acknowledged:

            # Splits the gameStatusText which is in the format 'Q4 5:00'
            quarter_and_Time = game['gameStatusText'].split(' ')
            
            # When the time is under a minute, the input is ":30" and this will cause a ValueError.
            try:
                quarterTime = datetime.strptime(quarter_and_Time[1], '%M:%S').minute
            except ValueError:
                # Sets to 1 minute as a usable value.
                quarterTime = 1
            except:
                print("Something else went wrong")

            # If there are 6 minutes or less in the last quarter and if the score between the two teams is 5 points or less.
            if quarterTime <= 7 and abs(home_team_score - away_team_score) <= 5 and quarterTime > 3:

                    # Appends home team to 'do not send' list.
                    games_acknowledged.append(home_team_name)

                    # Loads users to send signal to.
                    user_email = pd.read_csv('email_list.csv', index_col=0)

                    # Generates message to send via email
                    subject = 'Buzzer Beater$\n'
                    body = f"{home_team_name} ({home_team_score}) vs {away_team_name} ({away_team_score})"
                    msg = 'Subject: {}\n\n{}'.format(subject, body)

                    # Sends email to all users.
                    for email_str in user_email.index:
                        Delivery.sendEmail(email_str, msg)

    # Waits 30 seconds until the next iteration.
    time.sleep(30)

exit()
