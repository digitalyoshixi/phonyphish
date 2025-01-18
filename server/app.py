from flask import Flask, request, Response
#from flask_sock import Sock 
from twilio.twiml.voice_response import VoiceResponse, Connect, Stream
from flask_cors import CORS, cross_origin
from flask_sockets import Sockets
import json 

app = Flask(__name__) # designates this script as the root apth
sockets = Sockets(app)
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


@sockets.route('/realtime')
def echo_socket(ws):
    """Handle WebSocket connections"""
    print("can it be done? if not then try TLS")
    try:
        while not ws.closed:
            # Get message from WebSocket
            message = ws.receive()
            
            if message is None:
                continue
            
            # Process the audio stream here
            # For example, you could:
            # - Save the audio
            # - Perform real-time analysis
            # - Forward to another service
            
            # Echo back to confirm receipt
            ws.send(message)
            
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        if not ws.closed:
            ws.close()


if __name__ == "__main__": # if running this file directly
    app.run(host='0.0.0.0', port=8000, debug=True) # run the app
