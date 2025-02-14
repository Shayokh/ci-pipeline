from celery import Celery
import time
import pymongo

celery_app = Celery(
    "worker",
    broker="redis://redis:6379/0",
    backend=
    "mongodb://mongodb:27017/tasks"
)

# MongoDB client
client = pymongo.MongoClient("mongodb://mongodb:27017/")
db = client["celery_db"]
collection = db["task_results"]

@celery_app.task
def create_task(data):
    time.sleep(5)  # Simulate a long-running task
    result = {
        "data": data,
        "status": "completed"
    }
    collection.insert_one(result)
    return result
