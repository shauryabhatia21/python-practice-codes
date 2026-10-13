import os
from twilio.rest import Client

ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID', 'your_account_sid_here')
AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN', 'your_auth_token_here')
TWILIO_NUMBER = os.getenv('TWILIO_PHONE_NUMBER', '+18315316379')

def send_library_sms():
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    print("--- Library SMS Portal ---")
    raw_number = input("Enter the recipient's 10-digit mobile number: ").strip()
    if raw_number.startswith('+91'):
        target_number = raw_number
    elif len(raw_number) == 10 and raw_number.isdigit():
        target_number = f"+91{raw_number}"
    else:
        print(" Invalid Input: Please enter a valid 10-digit mobile number.")
        return
    try:
        print(f"Sending message to {target_number}...")
        message = client.messages.create(
            from_=TWILIO_NUMBER,
            body='HELLO MY NAME IS SHAURYA BHATIA,NICE TO MEET YOU',
            to=target_number
        )
        print(f"Success! Message sent successfully.")
    except Exception as e:
        print(f"Failed to send message.")
        print(f"Error Details: {e}")

if __name__ == "__main__":
    send_library_sms()
