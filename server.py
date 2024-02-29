# app.py
from flask import Flask, render_template
from flask_socketio import SocketIO,emit
from roomba_control import roombacontrol

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

roomba=roombacontrol()


@app.route('/')
def index():
    return render_template('uv4l.html')

@socketio.on('message')
def handle_message(message):
    # Just emit the received message to all connected clients except the sender
    print("message",message)
    roomba.docommand(message)
    emit('message', message, broadcast=True, include_self=False)
    

# WebSocket events for signaling would go here

if __name__ == '__main__':
    socketio.run(app, debug=True,host='0.0.0.0', port=5000)