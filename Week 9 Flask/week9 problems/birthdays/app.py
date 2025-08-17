import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SECRET_KEY"] = "dev"

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the user's entry into the database

        name = (request.form.get("name") or "").strip()
        months= (request.form.get("month") or "").strip()
        days = (request.form.get("day") or "").strip()

        check30 = [4, 6, 9, 11]
        check = True
        msg = ""



        if name == "" and check == True:
            msg = "Name input was blank"
            check = False

        if months == "" and check == True:
            msg = "Month input was blank"
            check = False

        if days == "" and check == True:
            msg = "day input was blank"
            check = False

        month = int(months)
        day   = int(days)

        if (month < 1 or month > 12) and check == True:
            msg = "please choose a month between 1 and 12"
            check = False

        if (day < 1 or day > 31) and check == True:
            msg = "Please choose a day between 1 and 31"
            check = False

        if month in check30 and check == True:
            if day > 30:
                msg = "The month you have selected has a max of 30 days"
                check = False

        if month == 2 and check == True:
            if day > 29:
                msg = "The max input for Month 2 is 29 days"
                check = False


        if check == False:
            flash(msg,"danger")
            return redirect("/")
        else:
            db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)",name,months,days)
            flash("New Birthday Added","success")
            return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html

        birthdays = db.execute("SELECT * FROM birthdays")

        return render_template("index.html", birthdays=birthdays)


