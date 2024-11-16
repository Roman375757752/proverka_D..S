from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

# Переменная для отслеживания количества посещений
visit_count = 0

@app.route('/')
def index():
    global visit_count
    visit_count += 1
    socketio.emit('update_count', {'count': visit_count}, broadcast=True)
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    # При подключении клиента отправляем текущее значение счётчика
    emit('update_count', {'count': visit_count})

if __name__ == '__main__':
    socketio.run(app, debug=True)
