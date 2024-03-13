# app.py
from flask import Flask, render_template
from flask_socketio import SocketIO,emit
#from roomba_control import roombacontrol
from roomba_control import *
from flask_cors import CORS
import threading
from multiprocessing import Process
import elara
import time

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app,cors_allowed_origins="*")

db = elara.exe("roomba.db")
db.set("direction", "")
db.set("battery", 100)

@app.route('/')
def index():
    return render_template('uv4l.html')

@socketio.on('connect')
def connected(message):
    print("connect",message)

@socketio.on('message')
def handle_message(message):
    global db
    # Just emit the received message to all connected clients except the sender
    print("got message",message)
    db.set("command", message)
    db.commit()
    emit('message-response', message, broadcast=True, include_self=False)
    

def updater(db):
    while True:
        emit('batterylevel', db.get("battery"), broadcast=True, include_self=False)
        time.sleep(5)


if __name__ == '__main__':
    p = Process(target=startroomba)  # Set up the child process with the queue
    p.start()  # Start the child process

    #run updater
    #x = threading.Thread(target=updater, args=(db,))
    #x.start()

    socketio.run(app, debug=True,host='0.0.0.0', port=5000)
    p.join()