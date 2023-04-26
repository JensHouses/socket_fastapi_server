import socketio  # python-socketio==5.8.0


sio = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins=['http://localhost:5173', 'https://wahlen.localhost']
)

sio_app = socketio.ASGIApp(
    sio,
    socketio_path='/'
)


@sio.event
async def connect(sid, environ):

    print('new connection. sid:', sid)
    await sio.emit('debug', {'status': 'Connected', 'sid': sid})
    return "welcome"


@sio.event
async def disconnect(sid):
    print('Session disconnected. sid:', sid)
    await sio.emit('debug', {'status': 'Disconnected', 'sid': sid})

@sio.event
async def subscribe(sid, data):
    print("sid: ", sid, 'subscribed to', data)
    sio.enter_room(sid, data)
    await sio.emit('debug', {'subscription_to': data, 'sid': sid})
    return 'Entered room: ' + data

@sio.event
async def unsubscribe(sid, data):
    print("sid: ", sid, 'unsubscribed to', data)
    sio.leave_room(sid, data)
    return 'Left room: ' + data
