from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Hello, Flask!"})

# Example of a route with parameters
@app.route('/user/<username>', methods=['GET'])
def user(username):
    return jsonify({"message": f"Hello, {username}!"})

if __name__ == '__main__':
    app.run(debug=True, port=5001)