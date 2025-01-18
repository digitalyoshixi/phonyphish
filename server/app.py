from flask import Flask, request, Response
from flask_sock import Sock 
from twilio.twiml.voice_response import VoiceResponse
from flask_cors import CORS, cross_origin
import json 

app = Flask(__name__) # designates this script as the root apth
sock = Sock(app)
CORS(app, supports_credentials=True, origins="*")
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        xml = f"""
<?xml version="1.0" encoding="UTF-8"?>
<Response><Say voice="woman">Helo the call is connected go speak now</Say><Connect><Stream url='wss://{request.host}/realtime'/></Connect></Response>
        """.strip()
        print(xml)
        return Response(xml, mimetype='text/xml')
    else:
        return "transcription testing"

@sock.route('/realtime')
def transcription_websocket(ws):
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
