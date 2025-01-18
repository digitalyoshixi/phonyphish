from flask import Flask, request, Response
from flask_sock import Sock 
from twilio.twiml.voice_response import VoiceResponse, Connect, Stream
from flask_cors import CORS, cross_origin
#from flask_sockets import Sockets
import json 
from datetime import datetime
import base64
import audioop
import speech_recognition as sr
import audioop
import json
from vosk import Model, KaldiRecognizer

# Load Vosk model
#model = Model("./vosk-model")
#rec = KaldiRecognizer(model, 16000) # apparently android devices have 16000Hz freq rate

#def decodemulaw(mulaw_data):
#    # Assume `mulaw_data` is your μ-law encoded audio data
#    raw_audio = audioop.ulaw2lin(mulaw_data, 2)  # Convert μ-law to linear PCM
#    if rec.AcceptWaveform(raw_audio):
#        result = json.loads(rec.Result())
#        print(result['text'])
#    else:
#        partial_result = json.loads(rec.PartialResult())
#        print(partial_result['partial'])

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
    print(ws)
    print("hello?")
    totalbytes = bytes()
    while True:
        data = json.loads(ws.receive())
        type = data['event']
        if type == "connected":
            print("connected")  
        if type == "start":
            print("start")  
        if type == "media":
            print("media")  
            payloadb64 = data['media']['payload']
            print(base64.b64decode(payloadb64))
            totalbytes += base64.b64decode(payloadb64)
            # decode the mulaw payload
            
        if type == "stop":
            print("stop")  
            f = open('temp', 'wb')
            f.write(totalbytes)
            f.close()

if __name__ == "__main__": # if running this file directly
    app.run(host='0.0.0.0', port=8000, debug=True) # run the app