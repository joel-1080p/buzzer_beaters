# NBA Buzzer Beater

## BUZZER BEATER STRATEGY
Buzzer Beeater looks for NBA games that are in the 4th quarter with 7 minutes left in the game.
If the score is within 5 points and above 5 minutes, it will send the signal via email.
The user can then place a bet that the game's score will end within 5 points.

![IMG_1507](https://github.com/joel-1080p/buzzer_beaters/assets/156847809/f521497b-36a8-41be-b8d4-4989a598c710)

## HOW TO USE IT
Set `buzzer_beaters.py` to run Monday through Saturday at 6PM during the NBA season.
In the `email_list.csv`, put all of the emails you'd like the signal to be sent to.
In `config.py`, put the email that's going to be sending the signal from.

NOTE : Look into setting an App Password for this to work.

## DELIVERY TOOLS
`delivery_tools.py` is a class I created to send signals in multiple ways.
You can send signals via 
- Discord
- Email
- SMS text

In `buzzer_beater.py`, under line 60, you can change the delivery method.

### P.S.

Please drop me a note with any feedback you have.

**Joel**
