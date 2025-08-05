from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room, emit
from datetime import datetime
import random
import string
import os 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super_secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat():
    room = request.args.get('room')
    if not room:
        return "Room code missing", 400
    return render_template('chat.html', room=room)

def generate_username():
    suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return f"node_0x{suffix}"

@socketio.on('join')
def handle_join(data):
    room = data.get('room')
    username = generate_username()
    if not room:
        return
    join_room(room)
    emit('user_joined', {'username': username}, room=room)
    emit('assign_username', {'username': username}, to=request.sid)

@socketio.on('send_message')
def handle_message(data):
    room = data.get('room')
    username = data.get('username')
    message = data.get('message')
    if not all([room, username, message]):
        return
    timestamp = datetime.now().strftime('%H:%M:%S')
    emit('receive_message', {
        'username': username,
        'message': message,
        'timestamp': timestamp
    }, room=room)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    print(f"Running on port {port}...")  # Add this debug log
    socketio.run(app, host="0.0.0.0", port=port, debug=True)
