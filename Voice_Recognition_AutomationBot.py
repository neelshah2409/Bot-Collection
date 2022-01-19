import smtplib
from email.message import EmailMessage

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

server_login_mail = "youremail@gmail.com"#enter your own email here,if it raises SMTPAuthenticationError(code, resp) then allow less secure apps in your email security settings to login using this script
server_login_password = "yourpassword13@$"#enter your own email password here
server.login(server_login_mail, server_login_password)