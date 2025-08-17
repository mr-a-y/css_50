
import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    user = session["user_id"]

    cash_row = db.execute("SELECT cash FROM users WHERE id = ?", user)[0]
    cash = cash_row["cash"]


    rows = db.execute("SELECT symbol, shares FROM portfolio WHERE user_id = ?", user)

    portfolio = []
    total = cash

    for r in rows:
        quote = lookup(r["symbol"]) or {"price": 0}
        price = quote["price"]
        position_total = price * r["shares"]

        portfolio.append({
            "symbol": r["symbol"],
            "shares": r["shares"],
            "price": usd(price),
            "total": usd(position_total)
        })

        total += position_total

    user_row = db.execute("SELECT username FROM users WHERE id = ?", user)[0]
    username = user_row["username"]

    flash(f"Welcome {username}")
    return render_template("index.html", portfolio = portfolio, cash = usd(cash), total= usd(total))



@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":
        if not request.form.get("symbol"):
            flash("Text-field left empty")
            return render_template("buy.html")

        symbol = request.form.get("symbol")

        if lookup(symbol) == None:
             return apology("Non Existent Stock ",400)


        quote = lookup(symbol)
        shares_str = (request.form.get("shares") or "").strip()

        if not shares_str.isdigit():
            return apology("shares must be a positive integer", 400)

        shares = int(shares_str)

        if shares < 1:
            return apology("shares must be at least 1", 400)


        user = session["user_id"]

        cash_row = db.execute("SELECT cash FROM users WHERE id = ?", user)[0]
        cash = cash_row["cash"]

        price = quote["price"] * shares

        if price > cash:
            flash(f" Your cash holding are {usd(cash)} which is lower Shares you are trying to buy at {usd(price)}")
            return render_template("buy.html")

        db.execute("INSERT INTO history (symbol, action, shares, purchase_price, user_id) VALUES (?, ?, ?, ?, ?)", symbol, "buy", shares, quote["price"], user) #history


        db.execute("UPDATE users SET cash = ? WHERE id = ?", (cash - price), user) # cash holding

        rows = db.execute("SELECT shares FROM portfolio WHERE user_id = ? AND symbol = ?", user, symbol) # check if user owns stock
        if rows:
            db.execute("UPDATE portfolio SET shares = shares + ? WHERE user_id = ? AND symbol = ?", shares, user, symbol) # add new share to existing
        else:
            db.execute("INSERT INTO portfolio (symbol, shares, user_id) VALUES (?, ?, ?)", symbol, shares, user) # add new entry if doesnt own

        flash(f"{shares} Shares of {symbol} have been purchased")
        return redirect("/")

    else:
        return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user = session["user_id"]

    history = db.execute("SELECT * FROM history WHERE user_id = ? ORDER BY created_at DESC", user)

    if len(history) < 1:
        return render_template("no_history.html")


    for x in history:
        x["purchase_price"] = usd(x["purchase_price"])

    return render_template("history.html",history = history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("Text-field left empty" ,400)


        symbol = request.form.get("symbol")

        if lookup(symbol) == None:
            return apology("Non Existent Stock ", 400)


        quote = lookup(symbol)

        flash("Stock Found")
        return render_template("quote.html", quote = quote)

    else:
       return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        elif not request.form.get("confirmation"):
            return apology("must provide confirmation", 400)

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if password != confirmation:
            return apology("password and confirmation arent the same", 400)

        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, generate_password_hash(password))
        except Exception:
            return apology("username already exists", 400)

        row = db.execute("SELECT id FROM users WHERE username = ?", username)
        session["user_id"] = row[0]["id"]

        flash(" Your account has been registered")
        return redirect("/")

    else :
        return render_template("register.html")




@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    user = session["user_id"]
    symbols = db.execute("SELECT * FROM portfolio WHERE user_id = ?",user)

    if request.method == "POST":
        shares = int(request.form.get("shares"))

        if shares < 1:
            return apology("must provide a number bigger then 1 ", 400)

        symbol = request.form.get("symbol")
        numbers = int(db.execute("SELECT shares FROM portfolio WHERE user_id = ? AND symbol = ? ", user, symbol)[0]["shares"])

        if not symbol:
            return apology("choose a symbol", 400)


        if shares > numbers:
            return apology(f"You only have {numbers} shares of {symbol}",400)

        quote = lookup(symbol)
        price = quote["price"] * shares

        db.execute("INSERT INTO history (symbol, action, shares, purchase_price, user_id) VALUES (?, ?, ?, ?, ?)", symbol, "sell", shares, quote["price"], user) #history
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", price, user) # updating the cash in the data base

        if shares == numbers:
            db.execute("DELETE FROM portfolio WHERE user_id = ? AND symbol = ?", user, symbol) # if there will be no shares left
        else:
            db.execute("UPDATE portfolio SET shares = shares - ? WHERE user_id = ? AND symbol = ?", shares, user, symbol) # if shares of the stock will be left

        flash(f"{shares} of {symbol} have been sold")
        return redirect("/")
    else:
        if len(symbols) < 1:
            return render_template("sell_nothing.html")
        return render_template("sell.html", symbols = symbols)

@app.route("/password", methods=["GET", "POST"])
@login_required
def pasword():
    """Change Password"""
    if request.method == "POST":
        user_id = session["user_id"]


        old = request.form.get("old")
        new_password = request.form.get("password")
        comfirm = request.form.get("confirmation")

        user = db.execute("SELECT * FROM users WHERE id = ?",user_id)[0]

        if not check_password_hash(user["hash"], old):
            flash("Your old Password is Incorect ")
            return render_template("password.html")
        if new_password != comfirm:
            flash("the Comfirmation and the new Password are not equal")
            return render_template("password.html")

        db.execute("UPDATE users SET hash = ? WHERE id = ?", generate_password_hash(new_password), user_id)
        flash("Password Updated")

        return redirect("/")
    else:
        return render_template("password.html")


