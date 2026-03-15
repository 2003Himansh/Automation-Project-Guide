import smtplib
from email.mime.text import MIMEText


class EmailAutomation:

    def send_email(self, sender, password, receiver, subject, message):

        msg = MIMEText(message)

        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = receiver

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

        server.login(sender, password)

        server.sendmail(sender, receiver, msg.as_string())

        server.quit()

        print("Email sent successfully")