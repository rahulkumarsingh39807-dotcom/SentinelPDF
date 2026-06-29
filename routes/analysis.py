
from flask import Blueprint, render_template
from flask_login import login_required

analysis = Blueprint("analysis", __name__)

@analysis.route("/upload")
@login_required
def upload():

    return render_template("analysis/upload.html")