import smtplib
from email.message import EmailMessage
import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server_login_mail = "youremail@gmail.com"  # enter your own email here,if it raises SMTPAuthenticationError(code, resp) then allow less secure apps in your email security settings to login using this script
server_login_password = "yourpassword13@$"  # enter your own email password here
server.login(server_login_mail, server_login_password)


def say(text):
    engine.say(text)
    engine.runAndWait()


say("hello sir, how can i help you? myself email assistant")


def assistant_listener():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            info = listener.recognize_google(voice, language="en-in").lower()
            return info

    except:
        return "no"


def send_email(rec, subject, message):
    email = EmailMessage()
    email["From"] = server_login_mail
    email["To"] = rec
    email["Subject"] = subject
    email.set_content(message)
    server.send_message(email)


contact = {
    "google": "google@gmail.com",
    # please add your contacts mails here
}


def whattodo():
    listen_me = assistant_listener()
    if "assistant" in listen_me:  # say "assistant to call the bot"
        if "write mail" in listen_me:
            say("To whom you want to send mail?")
            user = assistant_listener()
            try:
                email = contact[user]
            except:
                say(user + " not found in your contacts!")
                return 0
            say("What you want to be subject?")
            subject = assistant_listener()
            say("what should be the message?")
            message = assistant_listener()
            send_email(email, subject, message)
            say("Email Send Successfully")


while True:
    whattodo()
