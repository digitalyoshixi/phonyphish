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
        response.say("Hello, the call is connected. You may speak now.", voice="woman")
        # Start recording with transcription enabled
        response.record(
            timeout=5,  # Stop recording after 20 seconds of silence
            maxLength=300,  # Maximum recording length of 5 minutes
            playBeep=True,
            transcribe=True,  # Enable transcription
            transcribeCallback='/transcription_callback'  # Webhook for transcription results
        )
        response.hangup()

        return str(response)
    else:
        return "hi this is transcription testing, dont view this with a GET request"

@app.route("/transcription_callback", methods=['POST'])
def handle_transcription():
    """Handle the transcription callback from Twilio."""
    # Get the transcription data
    transcription_status = request.values.get('TranscriptionStatus')
    transcription_text = request.values.get('TranscriptionText')
    recording_url = request.values.get('RecordingUrl')
    
    if transcription_status == 'completed':
        # Store or process the transcription
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # Example: Save to a file
        with open(f'transcription_{timestamp}.txt', 'w') as f:
            f.write(f"Recording URL: {recording_url}\n")
            f.write(f"Transcription: {transcription_text}\n")
    
    return 'OK'



if __name__ == "__main__": # if running this file directly
    app.run(host='0.0.0.0', port=8000, debug=True) # run the app
