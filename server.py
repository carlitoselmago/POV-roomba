# app.py
from flask import Flask, render_template
from flask_socketio import SocketIO,emit
from roomba_control import roombacontrol
from flask_cors import CORS
import threading

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app,cors_allowed_origins="*")

def startroomba():
    robot = Create3(Bluetooth('MonicaRoomba'))

    @event(robot.when_play)
    async def play(robot):

        while self.moving:

            await robot.set_wheel_speeds(self.left,self.right )
    
    robot.play()

#roomba=roombacontrol()
roombathread = threading.Thread(target=startroomba)
roombathread.start()



@app.route('/')
def index():
    return render_template('uv4l.html')

@socketio.on('connect')
def connected(message):
    print("connect",message)

@socketio.on('message')
def handle_message(message):
    # Just emit the received message to all connected clients except the sender
    print("got message",message)
    #roomba.docommand(message)
    emit('message', message, broadcast=True, include_self=False)
    

# WebSocket events for signaling would go here

if __name__ == '__main__':
    socketio.run(app, debug=True,host='0.0.0.0', port=5000)