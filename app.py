from flask import Flask, render_template, request, jsonify, send_from_directory
from helpers.set_page_icons import page_icon
from Management.compare_texts import chercher_similarite_travail
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os
import threading
from werkzeug.serving import make_server

load_dotenv()

app = Flask(__name__, static_folder='static', template_folder='templates')

# Initialize ChatGroq client
api_key = os.getenv('GROQ_API_KEY')
if not api_key:
    api_key = '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'

client = ChatGroq(
    model="llama3-70b-8192",
    api_key=api_key,
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/chat_page', methods=['GET'])
def chat_page():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data['msg']
    full_prompt = chercher_similarite_travail(user_message)
    response = client.invoke(full_prompt).content
    return jsonify({'response': response})

@app.route('/session_ids', methods=['GET'])
def session_ids():
    return jsonify([])  # Placeholder

@app.route('/new_session', methods=['POST'])
def new_session():
    return jsonify({'session_id': 'new_session_id'})  # Placeholder

@app.route('/delete_session/<session_id>', methods=['DELETE'])
def delete_session(session_id):
    return jsonify({'success': True})  # Placeholder

@app.route('/load_chat_history/<session_id>', methods=['GET'])
def load_chat_history(session_id):
    return jsonify([])  # Placeholder

@app.route('/update_session_name', methods=['POST'])
def update_session_name():
    data = request.json
    session_id = data['session_id']
    new_session_name = data['new_session_name']
    return jsonify({'success': True})  # Placeholder

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

class ThreadedServer:
    def __init__(self, host, port, app):
        self.server = make_server(host, port, app)
        self.server_thread = threading.Thread(target=self._serve_forever)

    def _serve_forever(self):
        try:
            self.server.serve_forever()
        except OSError as e:
            print(f"Server error: {e}")

    def start(self):
        self.server_thread.start()

    def shutdown(self):
        self.server.shutdown()
        self.server_thread.join()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

