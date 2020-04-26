from celery import Celery
import time
app = Celery('tasks', broker='redis://redis:6379',
                      backend='redis://redis:6379')

app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='Europe/Oslo',
    enable_utc=True,
)


@app.task
def long_task(x, y):

    time.sleep(10)
    return "long_task"
