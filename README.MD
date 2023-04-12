# Socket Broadcasting Server

## Description

 This is a simple socket broadcasting server. It is written in Python 3.9.
 It uses the `socket.io` module to create a TCP socket server. 
 It uses the `threading` module to create a thread for each client that connects to the server.
 The server broadcasts `event` with `data` to all connected clients whitin a given `channel`. 
 The server also runs a Fastapi server to retrieve the `event`, `data` and `channel` to broadcast to.
 
## Installation

### Requirements

- Python 3.9
- venv
- Docker
- Docker-compose


### Setup local development environment

1. Clone the repository
2. Run `cd Folder` to go into the folder
3. Run `pyton3 -m venv venv` to create a new virtual environment
4. Run `source venv/bin/activate` to activate the virtual environment for unix like systems
5. Run `pip install -r requirements.txt` to install the required packages

### Setup production environment

1. Clone the repository
2. Run `cd Folder` to go into the folder
3. Run docker-compose up -d --build to build and run the docker container

## Usage

### Sending a broadcast

 The server runs a Fastapi server to receive the `event`, `data` and `channel` to broadcast to.
 the endpoint is `http://localhost:8000/broadcast/{channel}/{event}` and it accepts a `POST` request with the payload like:
 
JSON Payload:
 ```json
 {
    "data": "data_to_broadcast"
 }
 ```

String Payload:
 ```json
 "data_to_broadcast"
 ```

Integer Payload:
```json
123
```

Float Payload:
```json
123.45
```

Array Payload:
```json
["string", 123, 123.45, {"data": 12}]
```

When sending a `False` payload, the server will return a `422` error.
but the booleans `true` and `false` are valid payloads.

### Receiving a broadcast

 The server runs a socket server on the following endpoint `http://localhost:8000/socket.io`.
    The server uses the `socket.io` module to create the socket server.
    to subscribe to a channel, you need to emit the `subscribe` event with the channel name as the payload.
    to unsubscribe from a channel, you need to emit the `unsubscribe` event with the channel name as the payload.
    to receive a broadcast, you need to listen to the `event` name that you want to receive.
    the server will broadcast the `event` with the `data` to all connected clients within the given `channel`.


 ### Using Postman to test the server

1. Open Postman
2. Create a new request
3. Select the `Websocket Request` method (currently beta)
4. Select `Socket.io` as the protocol
5. Enter the following url `http://localhost:8000`
6. In Settings tab, select client_version as `4.0`
7. In Events tab, add event names to listen to
8. Click on `Connect`
9. In the `Messages` tab, you enter a channel name as your message
10. on the bottom right, check `Ack` and enter `subscribe` as the event name
11. Click on `Send`

You now subscribed to the channel and you will receive all broadcasts to that channel.
