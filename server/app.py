import time
import uvicorn
import os
import json
import base64
import asyncio
import websockets
from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import HTMLResponse
from fastapi.websockets import WebSocketDisconnect
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Connect
from dotenv import load_dotenv

# loading env environment
load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')

app = FastAPI()

@app.post("/make_call")
async def make_call(request : Request):
    data = await request.json()
    destphone = data.get("to")

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    call = client.calls.create(url="", to="a", from_=+18795039086)
    print(call.sid)

@app.api_route("/outgoing-call", methods=["GET", "POST"])
async def handle_outgoing_call(request: Request):
    """Handle outgoing call and return TwiML response to connect to Media Stream."""
    response = VoiceResponse()
    response.say("Please wait while we connect your call to the AI voice assistant...")
    connect = Connect()
    connect.stream(url=f'wss://{request.url.hostname}/media-stream')
    response.append(connect)
    return HTMLResponse(content=str(response), media_type="application/xml")

@app.websocket("/media-stream")
async def handle_media_stream(websocket: WebSocket):
    """Handle WebSocket connections between Twilio and OpenAI."""
    print("Client connected")
    await websocket.accept()

    async for message in websocket.iter_text():
        data = json.loads(message)
        if data['event'] == 'media':
            audio_append = {
               "type": "input_audio_buffer.append",
               "audio": data['media']['payload']
            }
            print(audio_append)
        elif data['event'] == 'start':
            stream_sid = data['start']['streamSid']
            print(f"Incoming stream has started {stream_sid}")

@app.get("/")
async def index():
    return {"message": "Twilio Media Stream Server is running!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)