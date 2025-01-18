from flask import Flask, request, Response
#from flask_sock import Sock 
from twilio.twiml.voice_response import VoiceResponse, Connect, Stream
from flask_cors import CORS, cross_origin
from flask_sockets import Sockets
import json 
from datetime import datetime

app = Flask(__name__) # designates this script as the root apth
sockets = Sockets(app)
CORS(app, supports_credentials=True, origins="*")
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        response = VoiceResponse()
        # Add initial greeting
        response.say("Helo, the call is connected go speak now.", voice="woman")
        # Start recording with transcription enabled
        connect = Connect()
        connect.stream(url='wss://ec2-54-234-22-87.compute-1.amazonaws.com:8000/transcription_callback')
        response.append(connect)
        return str(response)
    else:
        return "hi this is transcription testing, dont view this with a GET request"

@app.route("/transcription_callback", methods=['POST'])
def handle_transcription():
    """Handle the transcription callback from Twilio."""
    # Get the transcription data
    print("hi guys")
    return 'OK'



if __name__ == "__main__": # if running this file directly
    app.run(host='0.0.0.0', port=8000, debug=True) # run the app
