#!/usr/bin/env python3
import os, json, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

PAYLOAD_PATH = os.path.join(os.path.dirname(__file__), "..", "email_payload.json")

def main():
    with open(PAYLOAD_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    gmail_user = os.environ["GMAIL_USER"]
    gmail_pass = os.environ["GMAIL_APP_PASSWORD"]
    recipients = data["recipients"]
    msg = MIMEMultipart("alternative")
    msg["Subject"] = data["subject"]
    msg["From"] = gmail_user
    msg["To"] = ", ".join(recipients)
    msg.attach(MIMEText(data["htmlContent"], "html", "utf-8"))
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(gmail_user, gmail_pass)
        server.sendmail(gmail_user, recipients, msg.as_string())
    print("Email sent successfully to:", ", ".join(recipients))

if __name__ == "__main__":
    main()
