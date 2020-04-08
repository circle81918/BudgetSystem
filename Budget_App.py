from flask import Flask, escape, request, Response, send_from_directory
from flask_cors import CORS
from Budget_Manager import Budget_Manager
import json

class FlaskAppWrapper(object):
    def __init__(self, name, db_path = 'budget.db'):
        self.app  = Flask(name, static_url_path='', static_folder='UI')
        CORS(self.app)
        self.budget_manager = Budget_Manager(db_path)

    def run(self):
        self.registerAPI()
        self.app.run()

    def index(self):
        return send_from_directory('UI', 'index.html')

    def createBudget(self):
        json_data = request.get_json(force=True, silent=True)
        date = json_data['date']
        budget = json_data['budget']
        return Response(json.dumps({'message':self.budget_manager.createBudget(date, budget)}))

    def registerAPI(self):
        self.app.add_url_rule('/', 'index', self.index)
        self.app.add_url_rule('/createBudget/', 'createBudget', self.createBudget, methods=['POST',])
