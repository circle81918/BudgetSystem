from flask import Flask, escape, request, Response, send_from_directory
from flask_cors import CORS
from Budget_Manager import Budget_Manager
import json


app = Flask(__name__, static_url_path='', static_folder='UI')
CORS(app)
budget_manager = Budget_Manager(db_path='budget.db')

@app.route('/')
def index():
    return send_from_directory('UI', 'index.html')

@app.route('/createBudget/', methods=['POST'])
def createBudget():
    json_data = request.get_json(force=True, silent=True)
    date = json_data['date']
    budget = json_data['budget']
    return Response(json.dumps({'message':budget_manager.createBudget(date, budget)}))

if __name__ == '__main__':
    app.run()