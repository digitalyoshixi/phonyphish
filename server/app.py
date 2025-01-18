from flask import Flask, request, Response
from flask_sock import Sock 
from twilio.twiml.voice_response import VoiceResponse, Connect, Stream
from flask_cors import CORS, cross_origin
import json 

app = Flask(__name__) # designates this script as the root apth
sock = Sock(app)
CORS(app, supports_credentials=True, origins="*")
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        response = VoiceResponse()

        # Add initial greeting
        response.say("Hello, the call is connected. You may speak now.", voice="woman")

        # Connect the call to websocket
        connect = Connect()
        connect.stream(url=f'wss://{request.host}/realtime')
        response.append(connect)

        return str(response)
    else:
        return "hi this is transcription testing, dont view this with a GET request"

@sock.route('/realtime')
def transcription_websocket(ws):
    print("am i here and is this good?")
    while True:
        data = json.loads(ws.recieve())
        if data['event'] == "connected":
            print("twilio is ocnnected")
        elif data['event'] == "start":
            print("data stream start")
        elif data['event'] == "media":
            print("media block")
            payload = data['media']['payload']
            print(payload)
        elif data['event'] == "stop":
            print("data stream stop")


if __name__ == "__main__": # if running this file directly
    app.run(host='0.0.0.0', port=8000, debug=True) # run the app
