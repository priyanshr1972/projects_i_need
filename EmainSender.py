import smtplib as s
obj = s.SMTP("smtp.gmail.com",587)
obj.starttls()
mymail = open("Email_Id.txt")
Id = mymail.read()
password = open("Password.txt")
Pass = password.read()
obj.login(Id,Pass)
Message = open("message.txt")
message = Message.read()
teammails = open("Team_Id.txt")
Team_emails = []
str = " "
while(str):
    str = teammails.readline()
    Team_emails.append(str)
obj.sendmail(Id,Team_emails,message)
print("E-mail sent successfully...")
obj.quit()