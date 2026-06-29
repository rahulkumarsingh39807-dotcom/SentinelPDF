from flask import Blueprint, render_template, current_app
from flask import redirect, url_for, flash
from flask_login import login_required, current_user

from werkzeug.utils import secure_filename

import os

from forms import UploadPDFForm
from modules.hashes import calculate_hashes
from models import db, Analysis

analysis = Blueprint("analysis", __name__)

@analysis.route("/upload", methods=["GET", "POST"])
@login_required
def upload():

    form = UploadPDFForm()

    if form.validate_on_submit():

        file = form.pdf.data

        filename = secure_filename(file.filename)

        upload_path = os.path.join(
            current_app.config["UPLOAD_FOLDER"],
            filename
        )

        file.save(upload_path)

        hashes = calculate_hashes(upload_path)

        report = Analysis(
            filename=filename,
            md5=hashes["md5"],
            sha1=hashes["sha1"],
            sha256=hashes["sha256"],
            risk="Unknown",
            score=0,
            user_id=current_user.id
        )

        db.session.add(report)
        db.session.commit()

        flash("PDF uploaded successfully!", "success")

        return redirect(
            url_for(
                "analysis.result",
                analysis_id=report.id
            )
        )

    return render_template(
        "analysis/upload.html",
        form=form
    )


@analysis.route("/result/<int:analysis_id>")
@login_required
def result(analysis_id):

    report = Analysis.query.get_or_404(analysis_id)

    return render_template(
        "analysis/result.html",
        report=report
    )