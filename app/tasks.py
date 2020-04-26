from celery import Celery
import time
import logging

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
    logging.info('LOGGING {} {}'.format(epoch, arg))

@app.task
def long_task(x, y):

    time.sleep(10)
    return "long_task"
