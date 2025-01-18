# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()
# Set environment variables for your credentials
# Read more at http://twil.io/secure

account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH")
client = Client(account_sid, auth_token)

print(account_sid)
print(auth_token)


call = client.calls.create(
  url="http://demo.twilio.com/docs/voice.xml",
  to="+14168797536",
  from_="+16282031965"
)

print(call.sid)
