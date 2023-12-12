# worker.py
from rq import Worker, Queue, Connection
# from your_pdf_generation_module import pdf_generation_from_APIs
import os

listen = ['default']

# Redis connection
redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
conn = Connection(redis_url)
def generate_pdf():
    print("Task running ")

    
if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
