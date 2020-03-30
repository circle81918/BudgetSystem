from flask import Flask, escape, request, Response, send_from_directory
from flask_cors import CORS
import json


app = Flask(__name__, static_url_path='', static_folder='UI')
CORS(app)

@app.route('/')
def index():
    return send_from_directory('UI', 'index.html')

@app.route('/createBudget/', methods=['POST'])
def createBudget():
    json_data = request.get_json(force=True, silent=True)
    date = json_data['date']
    budget = json_data['budget']

    if date and budget:
        return Response(json.dumps({'message':'Create Budget Success'}))
    else:
        return Response(json.dumps({'message':'Create Budget Failure'}))

if __name__ == '__main__':
    app.run()