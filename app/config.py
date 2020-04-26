from pymongo import MongoClient

client = MongoClient('mongodb_container', 27017)
answer_db = client['answer_db']

answer_collection = answer_db.answer_collection

# answer_db.answer_collection.drop()

