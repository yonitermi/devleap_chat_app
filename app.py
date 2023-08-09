from flask import Flask, render_template, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

# Dictionary to store chat per room
chat_rooms = {}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<room>')
def room(room):
    return render_template('index.html')


@app.route('/api/chat/<room>', methods=['GET'])
def get_chat(room):
    if room in chat_rooms:
        return '\n'.join(chat_rooms[room])
    return '', 200


@app.route('/api/chat/<room>', methods=['POST'])
def post_chat(room):
    if room not in chat_rooms:
        chat_rooms[room] = []

    username = request.form.get('username')
    message = request.form.get('msg')
    time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    chat_line = f"[{time_stamp}] {username}: {message}"

    chat_rooms[room].append(chat_line)
    return '', 204  # Return No Content status


if __name__ == '__main__':
    app.run(debug=True)
