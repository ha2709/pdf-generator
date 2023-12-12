# app.py
from flask import Flask, request, jsonify
from rq import Queue
from redis import Redis

# from worker import generate_pdf
from services.pdf_generation import pdf_generation_from_APIs

# from flask_socketio import SocketIO
import uuid

redis_instance = Redis()
app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET_KEY"

q = Queue(connection=redis_instance)
# socketio = SocketIO(app)


@app.route("/")
def index():
    return jsonify({"status": "success", "message": "Hello World"})


@app.route("/generate_pdf", methods=["POST"])
def generate_pdf():
    try:
        data = request.json

        # Get data from the POST request
        pdf_data = data.get("pdf_data")
        pdf_uuid = str(uuid.uuid4())

        print(25, pdf_data, pdf_uuid)
        # Enqueue the PDF generation job

        job = q.enqueue(pdf_generation_from_APIs, pdf_data, pdf_uuid)

        print(27, "pdf_id", pdf_uuid)
        # Respond with a job ID that can be used to check the job status
        return jsonify({"status": "success", "pdf_uuid": pdf_uuid})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


if __name__ == "__main__":
    # socketio.run(app, debug=True)
    app.run(debug=True)
