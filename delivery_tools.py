import smtplib
import requests
import config

################################
################################
################################
################################
class Delivery:
    
    ################################
    ################################
    # Sends signal via email.
    # Takes in an email address and signal as strings.
    def sendEmail(receiver_email_address: str, body: str):

        # Algo credit - https://www.google.com/search?sxsrf=ALiCzsbABYoj5xPdbPvwfr1p_R6HrBONZw:1657166767037&q=receiver&spell=1&sa=X&ved=2ahUKEwjC6-2j8-X4AhWAjIkEHY2lA8YQBSgAegQIARA0&biw=1422&bih=765&dpr=1.8

        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)
        
        # start TLS for security
        s.starttls()
        
        # Authentication
        s.login(config.email, config.email_pw)

        # sending the mail
        s.sendmail(config.email, receiver_email_address, body)
        
        # terminating the session
        s.quit()

        return


    ################################
    ################################
    # Sends SMS via email.
    # Takes phone number, signal, and carrier as strings.
    def sendSMS(phone_number: str,  body: str, carrier: str):

        # Holds the domain based on the carrier.
        domain = ''

        #Applies the correct domain to the carrier
        match carrier:
            case 'verizon':
                domain = '@vtext.com'
            case 'atnt':
                domain = '@mms.att.net'
            case 'tmobile':
                domain = '@tmomail.net'
            case 'sprint':
                domain = '@pm.sprint.com'
            case 'virgin':
                domain = '@vmobl.com'
            case 'boost':
                domain = '@myboostmobile.com'
            case 'cricket ':
                domain = '@mms.cricketwireless.net'
            case 'us_cellular':
                domain = '@mms.uscc.net'
            case _:
                print('Carrier Does not exist.')
                return 0
        
        # Appends phone number to domain.
        email = phone_number + domain

        # Sends signal via email to the phone as SMS.
        Delivery.sendEmail(email, body)

        return
    

    ################################
    ################################
    # Sends signal to Discord.
    # Takes in the Discord URL, signal, the name of the bot and the URL logo for the bot as strings.
    # If no logo URL is provided, the function will not set one.
    def sendToDiscord(discord_url: str, signal: str, bot_name: str, logo_url: str):

        # Algo credit https://github.com/lth-elm/tradingview-webhook-trading-bot

        # In case the user does not want to use a logo URL.
        if logo_url == 'NA':
            message = {"username":bot_name,"content":signal}
        else:
            # Creates the message. Content being the the processed tickers, and username being name to appear.
            message = {"content":signal,
            "username":bot_name,
                    "avatar_url":logo_url
                    }

        # Sends the request to Discord.
        try:
            requests.post(discord_url, json=message)
            if error:
                requests.post(discord_url, json=message) 
        except:
            pass

        return