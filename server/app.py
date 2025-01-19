from flask import Flask, request, Response
from flask_sock import Sock 
from twilio.twiml.voice_response import VoiceResponse, Connect, Stream
from flask_cors import CORS, cross_origin
#from flask_sockets import Sockets
import json 
from datetime import datetime
import speech_recognition as sr
import audioop
import json
from vosk import Model, KaldiRecognizer

app = Flask(__name__) # designates this script as the root apth
sock= Sock(app)
CORS(app, supports_credentials=True, origins="*")
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        response = VoiceResponse()
        # Add initial greeting
        response.say("Helo, the call is connected you can speak now.", voice="woman")
        # Start recording with transcription enabled
        response.record(transcribe=True, transcribe_callback="/transcription")

        response.hangup()
        return str(response)
    else:
        return "hi this is transcription testing, dont view this with a GET request"

@app.route("/transcription", methods=["POST"])
def transcription():
    transcription_text = request.form.get("TranscriptionText")
    print(f"Transcription: {transcription_text}")
    
    # Optional: Send the transcription via SMS or store it in a database
    return "Transcription received"

