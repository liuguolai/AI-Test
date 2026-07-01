import os,json,smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
d=json.load(open("email_payload.json",encoding="utf-8"))
u,p=os.environ["GMAIL_USER"],os.environ["GMAIL_APP_PASSWORD"]
r=d["recipients"]
m=MIMEMultipart("alternative")
m["Subject"]=d["subject"];m["From"]=u;m["To"]=", ".join(r)
m.attach(MIMEText(d["htmlContent"],"html","utf-8"))
with smtplib.SMTP_SSL("smtp.gmail.com",465) as s:
 s.login(u,p);s.sendmail(u,r,m.as_string())
print("sent",r)
