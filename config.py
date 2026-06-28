import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "change-this-secret-key")
    SQLALCHEMY_DATABASE_URI = "sqlite:///sentinelpdf.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = "uploads"
    REPORT_FOLDER = "reports"

    MAX_CONTENT_LENGTH = 20 * 1024 * 1024

    ALLOWED_EXTENSIONS = {"pdf"}