import smtplib

def sendEmail(to, body):

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("arghya17112002@gmail.com", "Google_2020")
    server.sendmail("arghya17112002@gmail.com", to, body)
    server.close()


if __name__ == '__main__':

    i = int(input("Enter number to reciever"))
    body = input("Input email body")

    for i in range(i):

        to = input("Input email address to which email should be sent")
        sendEmail(to, body)