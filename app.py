# app.py
from flask import Flask, request, jsonify, render_template, send_from_directory, abort
from rq import Queue
from redis import Redis
from models.pdf_link import db, PDFLink
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


@app.route('/pdf-link/<uuid>', methods=['GET'])
def check_pdf_link_status(uuid):
    try:
        pdf_link = PDFLink.query.filter_by(uuid=uuid).first()

        if pdf_link is None:
            abort(404)  # PDF link not found

        if pdf_link.status == 'success':
            return render_template('pdf_download.html', pdf_link=pdf_link)
        else:
            return render_template('pdf_status.html', pdf_link=pdf_link)

    except Exception as e:
        # Handle the exception, log, or report it as needed
        return str(e)

@app.route('/download-pdf/<uuid>', methods=['GET'])
def download_pdf(uuid):
    try:
        pdf_link = PDFLink.query.filter_by(uuid=uuid).first()

        if pdf_link is None or pdf_link.status != 'success':
            abort(404)  # PDF link not found or status is not 'success'

        return send_from_directory(app.config['PDF_DOWNLOAD_PATH'], f"{uuid}.pdf", as_attachment=True)

    except Exception as e:
        # Handle the exception, log, or report it as needed
        return str(e)


if __name__ == "__main__":
    # socketio.run(app, debug=True)
    app.run(debug=True)
