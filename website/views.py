from flask import Blueprint, render_template, request, current_app, redirect, url_for, flash
from flask_mail import Mail, Message
from website.models import Categories
from website.helper_funcs import sort_search as ss
from website import attrs

views = Blueprint("views", __name__)


@views.route("/", methods=["GET"])
def home():
    return render_template("home.html", user="everyone")


@views.route("/topics", methods=["GET", "POST"])
def topics():
    if request.method == "GET":
        search = request.args.get("jsdata")
        state = request.args.get("state")
        topics = Categories.query.all()
        topics, search, state = ss.show(topics, search, state)

    else:
        search = request.form.get("search_filter")
        state_change = int(request.form.get("state_change_topics"))
        state = int(request.form.get("state_topics"))
        topics = Categories.query.all()
        topics, search, state = ss.show(topics, search, state, state_change)

    return render_template("topics.html", topics=topics, state=state, search=search)


@views.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        email = request.form.get("email")
        subject = request.form.get("subject")
        body = request.form.get("email_body")
        mail = Mail(current_app)
        msg = Message("Email from reader: " + subject, recipients=[attrs.PORTFOLIO_EMAIL])
        msg.body = body + "\nContact: " + email
        mail.send(msg)
        flash("Thank you for your email", category="success")
        return redirect(url_for("views.home"))
    else:
        return render_template("contact.html")
