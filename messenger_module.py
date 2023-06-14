import fbchat
import datetime


def getting_time_date():  # getting time and date to send the message
    year = int(input("enter the year"))
    month = int(input("enter the month"))
    date = int(input("enter the date"))
    hours = int(input("enter the hours"))
    minutes = int(input("enter the minutes"))
    seconds = int(input("enter the seconds"))
    send_time = datetime.datetime(year, month, date, hours, minutes, seconds)
    return send_time


def difference_in_seconds(send_time):
    curr_time = datetime.datetime.now()
    difference = send_time - curr_time
    seconds = difference.total_seconds()
    return seconds


send_time = getting_time_date()
seconds = difference(send_time)
if seconds < 0:
    print("Invalid send time, give a time in future not in past")
else:
    while True:
        time.sleep(seconds)
        username = input("Username: ")  # Enter the username
        client = fbchat.Client(username, getpass())
        name = input(
            "Name: "
        )  # Enter the friends username you wish to send the message
        friends = client.searchForUsers(name)  # return a list of names
        friend = friends[0]
        message = input("Message: ")  # Enter the input message that needs to be send
        sent = client.sendMessage(message, thread_id=friend.uid)
        if sent:
            print("Message sent successfully!")

        break
