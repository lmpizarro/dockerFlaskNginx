from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

import pymongo
import datetime

from tasks import long_task

from pymongo import MongoClient

client = MongoClient('mongodb_container', 27017)
answer_db = client['answer_db']

answer_collection = answer_db.answer_collection

answer_db.answer_collection.drop()

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello, World!'

api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('answer')


import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in results:
        abort(404, message="Todo {} doesn't exist".format(todo_id))


class Result(Resource):
    def get(self, result_id):
        abort_if_todo_doesnt_exist(result_id)
        return results[result_id].get(timeout=1) 


class Answer(Resource):

    def get(self):
        return JSONEncoder().encode({'id_': [answer for answer in answer_collection.find()]})
 
    def post(self):
        args = parser.parse_args()
        
        result = long_task.delay(4,4)        

        
        resp_id = answer_collection.insert_one({'answer': args['answer'], 
                                                'result_id': str(result.id),
                                                'date_time': datetime.datetime.now().__str__()}) 

        # resp['resp_id'] = resp_id
        
        

        resp = {'answer': args['answer'], 
                'result_id': str(result.id), 
                'counts': answer_collection.count_documents({})}
        
        return resp, 201


api.add_resource(Answer, '/answer')
api.add_resource(Result, '/result/<result_id>')



if __name__ == '__main__':
    app.run(debug=True)


