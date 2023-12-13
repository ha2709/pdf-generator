# models.py
import uuid
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PDFLink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(255), nullable=False)
    uuid = db.Column(db.String(36), unique=True, nullable=False, default=str(uuid.uuid4()))

    def __init__(self, link, uuid=None):
        self.link = link
        if uuid is not None:
            self.uuid = uuid
