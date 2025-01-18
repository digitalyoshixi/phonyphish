from flask import Flask, request, Response
from flask_sock import Sock 
from twilio.twiml.voice_response import VoiceResponse, Connect, Stream
from flask_cors import CORS, cross_origin
#from flask_sockets import Sockets
import json 
from datetime import datetime

app = Flask(__name__) # designates this script as the root apth
sock= Sock(app)
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
        connect.stream(url=f'wss://{request.host}/transcription_callback')
        response.append(connect)
        return str(response)
    else:
        return "hi this is transcription testing, dont view this with a GET request"

@sock.route('/transcription_callback')
def transcription_callback(ws):
    while True:
        data = json.loads(ws.recieve())
        type = data['event']
        if type == "connected":
            print("connected")  
        if type == "start":
            print("start")  
        if type == "media":
            print("media")  
            payload = data['media']['payload']
            print(payload)
        if type == "stop":
            print("stop")  


if __name__ == "__main__": # if running this file directly
    app.run(host='0.0.0.0', port=8000, debug=True) # run the app
