import smtplib
from email.message import EmailMessage

# Configuration
EMAIL_ADDRESS = "your-email@gmail.com"
EMAIL_PASSWORD = "your-16-char-app-password"

def send_me_email(subject, body):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS  # Sending to yourself
    msg.set_content(body)

    # Connecting to Gmail's SMTP server
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
send_me_email("Fit-Check-API Alert", "The stock scanner found a major gainer!")