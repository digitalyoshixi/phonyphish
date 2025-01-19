from flask import Flask, request, Response
from flask_sock import Sock 
from twilio.twiml.voice_response import VoiceResponse, Connect, Stream
from flask_cors import CORS, cross_origin
#from flask_sockets import Sockets
from datetime import datetime
import speech_recognition as sr
import json
from invokeEndpoint import invoke_endpoint
import dataretrieval

app = Flask(__name__) # designates this script as the root apthim
sock= Sock(app)
CORS(app, resources={r"/*" : {"origins" : "http://ec2-184-73-58-196.compute-1.amazonaws.com:8000"}})

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

@app.route('/invokeAI', methods=['POST'])
def invokeAI():
    if request.method == 'POST':
        print(request.method)
        print(invoke_endpoint(request.get_json()["message"])[0])

@app.route("/dbupdate", methods=["POST"])
def dbupdate():
    for k,v in request.get_json().items():
        print(f"{k} {v}")
        dataretrieval.update_cursor(
            phone_number=k,
            is_scam=v     
        ) 
    return "all good man"

@app.route("/dbinsert", methods=["POST"])
def dbinsert():
    for k,v in request.get_json().items():
        print(f"{k} [v]")
        is_scam = 1
        if invoke_endpoint(v) == "benign":
            is_scam = 0
        print (invoke_endpoint(v))
        dataretrieval.insert_cursor(
            phone_number=k,
            is_scam=is_scam,
            transcription=v
        ) 
    return "all good man"

@app.route("/dbview", methods=["GET"])
def dbview():
    return dataretrieval.read_cursor()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
