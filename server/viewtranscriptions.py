import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()
# Set environment variables for your credentials
# Read more at http://twil.io/secure

account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH")
client = Client(account_sid, auth_token)

# Fetch the latest transcription
transcriptions = client.transcriptions.list(limit=1)
if transcriptions:
    latest_transcription = transcriptions[0]
    breakpoint()
    print(latest_transcription.transcription_text)
