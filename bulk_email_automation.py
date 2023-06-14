import smtplib


def getting_login_credentials():
    email = input("Enter your email address")
    password = input("Enter password")
    return email, password


def getting_senders_email_address():
    n = int(input("enter the number of users"))
    emails = []
    for i in range(n):
        email = input("enter the email")
        emails.append(email)
    return emails


def getting_message_to_send():
    message = input("Enter the message")
    return message


def sending_automated_mails(email, password, receiver_emails, message):
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(email, password)
    to = receiver_emails
    smtp.sendmail(from_addr=email, to_addrs=to, msg=message)
    smtp.quit()

    email, password = getting_login_credentials()
    receiver_emails = getting_senders_email_address()
    message = getting_message_to_send()
    sending_automated_mails(email, password, receiver_emails, message)
