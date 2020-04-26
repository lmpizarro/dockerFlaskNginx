from celery import Celery
import time
import logging

from config import answer_collection
from bson.objectid import ObjectId

app = Celery('tasks', broker='redis://redis:6379',
                      backend='redis://redis:6379')

app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='Europe/Oslo',
    enable_utc=True,
)

from celery.schedules import crontab

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test_periodic.s(time.time(), 'hello'), name='add every 10')



@app.task
def test_periodic(epoch, arg):
    logging.info('LOGGING {} {} registers {}'.format(epoch, arg, answer_collection.count_documents({})))

@app.task
def long_task(x, y, resp_id):

    y = ObjectId(resp_id)
    r = [u for u in answer_collection.find({"_id": y})]

    logging.info('LOGGING Id {} {}'.format(resp_id, r))    
    time.sleep(10)
    return "long_task"
