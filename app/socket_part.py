import socketio  # python-socketio==5.8.0


sio = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins=['http://localhost:5173']
)

sio_app = socketio.ASGIApp(
    sio,
    socketio_path='/'
)


@sio.event
async def connect(sid, environ):
    print("--'--"*20)
    print('connection sid:', sid)

    #await sio.save_session(sid, {'username': "Test username"})
    await sio.emit('debug', {'status': 'Connected', sid: sid})

    return "welcome"


@sio.event
async def disconnect(sid):
    session = await sio.get_session(sid)
    print("--'--"*20)
    print(session.get("username", "--"), 'disconnect ', sid)
    await sio.emit('debug', {'status': 'Disconnected', 'sid': sid})

@sio.event
async def subscribe(sid, data):
    print("--'--"*20)
    print("subscribe sid: ", sid)
    print("subscribe data: ", data)
    sio.enter_room(sid, data)
    await sio.emit('debug', {'subscription_to': data, sid: sid})
    return 'Entered room: ' + data

@sio.event
async def unsubscribe(sid, data):
    print("--'--"*20)
    print("unsubscribe sid: ", sid)
    print("unsubscribe data: ", data)
    sio.leave_room(sid, data)
    return 'Left room: ' + data


