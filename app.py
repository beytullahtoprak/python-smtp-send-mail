from smtplib import SMTP
import password

# Simple Mail Taransfer Protocol

try:
    # Send Mail
    subject = "Demo"
    message = "Hi! How are you? This is message!"
    content = "Subject: {0}\n\n".format(subject,message)

    #mail info
    userMail = password.userMail
    userPass = password.userPass

    #who send mail
    sendTo = "whomail@gmail.com"

    mail = SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(userMail,userPass)
    mail.sendmail(userMail, sendTo, content.encode("utf-8"))
    print("Mail send successful...")

except Exception as e:
    print("Error Message:\n {0}".format(e))
