# app.py
from flask import Flask, render_template
from flask_socketio import SocketIO,emit
#from roomba_control import roombacontrol
from roomba_control import *
from flask_cors import CORS
import threading
from multiprocessing import Process, Queue


from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.backend.bluetooth import Bluetooth

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app,cors_allowed_origins="*")



@app.route('/')
def index():
    return render_template('uv4l.html')

@socketio.on('connect')
def connected(message):
    print("connect",message)

@socketio.on('message')
def handle_message(message):
    global q
    # Just emit the received message to all connected clients except the sender
    print("got message",message)
    #roomba.docommand(message)
    q.put(message)
    emit('message', message, broadcast=True, include_self=False)
    

# WebSocket events for signaling would go here

if __name__ == '__main__':
    q = Queue(maxsize=10)  # Create a queue
    p = Process(target=startroomba, args=(q,))  # Set up the child process with the queue
    p.start()  # Start the child process
    socketio.run(app, debug=True,host='0.0.0.0', port=5000)
    #p.join()