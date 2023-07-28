from flask import Blueprint, render_template

bp = Blueprint("index", __name__, template_folder="../templates")


@bp.route("/")
def Index():
    return render_template("index.html")
