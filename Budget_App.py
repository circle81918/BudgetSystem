from flask import Flask, escape, request, Response, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_url_path='', static_folder='UI')
CORS(app)

@app.route('/')
def hello():
    # name = request.args.get("name", "World")
    # return f'Hello, {escape(name)}!'
    return send_from_directory('UI', 'index.html')

if __name__ == '__main__':
    app.run()