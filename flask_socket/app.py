from flask_socketio import SocketIO, emit, send
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'something'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast = True)

if __name == '__main__':
    socketio.run(app)
