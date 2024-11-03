from flask import Flask, jsonify, request, send_from_directory, send_file
from flask_cors import CORS

from index import getAudioFile
app = CORS(Flask(__name__))


@app.route('/submit', methods=['POST'])
def home():
    videourl = request.form.get("videoname")
    filename = getAudioFile(videourl)
    print(videourl)
    return send_from_directory('.', {filename})

# Example of a route with parameters
@app.route('/download-song')
def download_song():
    return send_file('song.mp3', as_attachment=True, download_name='song.mp3')

if __name__ == '__main__':
    app.run(debug=True, port=5001)