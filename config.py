import os

class Config:

    SECRET_KEY="SentinelPDF2026"

    SQLALCHEMY_DATABASE_URI="sqlite:///sentinelpdf.db"

    SQLALCHEMY_TRACK_MODIFICATIONS=False

    UPLOAD_FOLDER="uploads"

    REPORT_FOLDER="reports"                                                            