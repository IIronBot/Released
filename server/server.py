from flask import Flask, jsonify, request, send_from_directory, send_file
from flask_cors import CORS
import os

from index import getAudioFile
app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Hello"
@app.route('/submit', methods=['POST'])
def sendAudioFile():
    videourl = request.form.get("videoname")
    filename = getAudioFile(videourl)
    print(videourl)
    return send_from_directory('.', {filename})

# Example of a route with parameters
@app.route('/download-song')
def download_song():
    return send_file('song.mp3', as_attachment=True, download_name='song.mp3')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=False)