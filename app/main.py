from fastapi import FastAPI, Body
from socket_part import sio_app, sio

app = FastAPI()
app.mount("/socket.io", sio_app)


@app.post("/broadcast/{channel}/{event}")
async def login(channel: str, event: str,
                data=Body(default={'data': 'to be send'}, description="Data to send")
                ):
    await sio.emit(event, data, room=channel)
    return {
        "Event": event,
        "channel": channel,
        "data": data
    }
