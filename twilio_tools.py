
from twilio.rest import Client


def send_message(msg, num):
    account_sid = 'AC308fdad4243a97c749cec2cbbeef6576'
    auth_token = 'd5440ad5f611c495603cf50912c91038'
    client = Client(account_sid, auth_token)



    message = client.messages \
                    .create(
                        #  body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                        body = msg,
                        from_='+15097740268',
                        to = '+1' + str(num)
                        #  to='+15157718408'
                    )

    print(message.sid)

