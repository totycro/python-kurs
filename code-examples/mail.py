
from email.message import EmailMessage
import smtplib


server = smtplib.SMTP("mail.gmx.net")
server.set_debuglevel(1)
server.starttls()
server.ehlo()
server.login("b.mallinger@gmx.at", open("pw").read())
server.ehlo()

sender = "b.mallinger@gmx.at"
rcv = "malli@gmx.at"

msg = f"""From: {sender}
To: {rcv}
Subject: foo

test
test
"""

#server.sendmail("malli@gmx.at", "malli@gmx.at", msg)

msg = EmailMessage()
msg['From'] = sender
msg['To'] = rcv
msg['Subject'] = "about the stuff"
msg.set_content("here's the stuff")

msg.add_attachment(open("file.pdf", "rb").read(), maintype="application/pdf", subtype="pdf", filename="a.pdf")


server.send_message(msg)

server.quit()


