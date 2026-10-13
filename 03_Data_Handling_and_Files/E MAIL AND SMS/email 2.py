import os
import smtplib

sender_email = os.getenv('EMAIL_SENDER', 'shauryabhatia133@gmail.com')
password = os.getenv('EMAIL_APP_PASSWORD', 'your_app_password_here')
receiver_email = input("Enter receiver email: ")
name = input("Enter registered name: ")
book = input("Enter book name: ")
date = input("Enter date of joining (DD-MM-YYYY): ")
subject = "THANK YOU FOR JOINING IN LIBRARY"
message = f"""Thank you for being a valuable customer in our library.
Here are your registration details:
- Registered Name: {name}
- Book Name: {book}
- Date of Joining: {date}
- Registered Email Address: {receiver_email}"""
text = f"Subject: {subject}\n\n{message}"
try:
    print("\nConnecting to Gmail's server...")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    print("Encrypting the connection...")
    server.starttls() 
    print("Logging in...")
    server.login(sender_email, password)
    print("Sending library welcome email...")
    server.sendmail(sender_email, receiver_email, text)
    print(f"\n Email successfully sent to {receiver_email}!")
except Exception as e:
    print(f"\n Failed to send email. Error: {e}")
finally:
    try:
        server.quit()
    except:
        pass
