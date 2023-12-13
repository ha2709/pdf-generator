from flask_socketio import SocketIO, emit
from models.pdf_link import db, PDFLink
import requests

bucket_name = "1234"


def pdf_generation_from_APIs(pdf_data, pdf_uuid):
    try:
        # Call APIs and get the PDF content
        # ...
        print(11, pdf_data)
        # resp = requests.get(url)
        # resp.text.split()
        new_pdf_link = PDFLink(link=pdf_link, uuid=pdf_uuid, status='pending')
        db.session.add(new_pdf_link)
        db.session.commit()
        file_key = pdf_uuid + ".pdf"
        # Save the S3 link and user_id to the database
        pdf_link = f"https://{bucket_name}.s3.amazonaws.com/{file_key}"
        print(14, pdf_link)
        new_pdf_link.link = pdf_link
        new_pdf_link.status = 'success'
        db.session.commit()

        return "PDF generation and upload to S3 completed successfully"
    except Exception as e:
        return str(e)
