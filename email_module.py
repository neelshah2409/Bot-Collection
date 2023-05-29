import smtplib
from email.message import EmailMessage

# This program/method takes in a subject, body and recepient to send text and email notifications
# for additional context: https://www.youtube.com/watch?v=B1IsCbXp0uE
def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg["subject"] = subject
    msg["to"] = to

    # email created for this purpose and application password bypassing MFA
    user = "insert email here"
    password = "insert generated password here"

    msg["from"] = user

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)

    server.send_message(msg)

    server.quit


# test 2 testing email and text message capabilities
if __name__ == "__main__":
    email_alert("Hey", "Test Email", "receiver")
    email_alert("Hey", "Test Message", "phone number@ cell provider receiver")
