from flask import Flask, request, Response
from flask_sock import Sock 
from twilio.twiml.voice_response import VoiceResponse
from flask_cors import CORS, cross_origin

app = Flask(__name__) # designates this script as the root apth
sock = Sock(app)
CORS(app, supports_credentials=True, origins="*")
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        xml = f"""
        <?xml version="1.0" encoding="UTF-8"?>
        <Reponse>
            <Say voice="woman">
                You have connected to flask
            </Say>
        </Reponse>
        """.strip()
        print(xml)
        return Response(xml, mimetype='text/xml')
    else:
        return "transcription testing"

@sock.route('/realtime')
def transcription_websocket(ws):
    pass

#@app.route("/answer", methods=['GET', 'POST'])
#def answer_call():
#    resp = VoiceResponse()
#    resp.say("Thank you for calling! Have a great day.", voice='Polly.Amy')
#    return str(resp)

if __name__ == "__main__": # if running this file directly
    app.run(host='0.0.0.0', port=8000, debug=True) # run the app
