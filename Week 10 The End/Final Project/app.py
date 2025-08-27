import sqlite3
from datetime import date, datetime, timedelta

from flask import Flask, flash, g, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helper import login_required, get_teams  

app = Flask(__name__)

app.secret_key = "change-me"

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect("sports.db", check_same_thread=False)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON;")
    return g.db

@app.teardown_appcontext
def close_db(exc):
    db = g.pop("db", None)
    if db is not None:
        db.close()

@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    current_date = date.today()
    if request.method == "POST":

        date_str = request.form.get("date") or date.today().strftime("%Y-%m-%d")
        current_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        action = request.form.get("action")

        if action == "prev":
            current_date -= timedelta(days=1)

        elif action == "next":
            current_date += timedelta(days=1)


    else:
        qs = request.args.get("date")
        if qs :
          current_date = datetime.strptime(qs, "%Y-%m-%d").date()   
        else:
            current_date = date.today()

    current_date_display = current_date.strftime("%A, %B %d, %Y")
    current_date_raw = current_date.strftime("%Y-%m-%d")

    db = get_db()
    rows = db.execute("SELECT team_id FROM nba_teams WHERE id IN (SELECT nba_id FROM my_teams WHERE user_id = ?)",(session["user_id"],)).fetchall()
    if not rows:
        return render_template("index.html", current_date_display=current_date_display, current_date_raw=current_date_raw, teams=[])

    ids = [] 
    for row in rows: 
        ids.append(row[0])

    teams = get_teams(current_date_raw, ids)

    return render_template( "index.html", current_date_display=current_date_display, current_date_raw=current_date_raw, teams=teams)


@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if not username:
            flash("must provide username", "warning") 
            return render_template("login.html")
        if not password:
            flash("must provide password", "warning") 
            return render_template("login.html")

        db = get_db()
        rows = db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchall()
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            flash("invalid username and/or password", "danger")
            return render_template("login.html")

        session["user_id"] = rows[0]["id"]
        return redirect("/")
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        confirmation = request.form.get("confirmation", "")

        if not username:
            flash("must provide username", "warning") 
            return render_template("register.html")
        if not password:
            flash("must provide password", "warning") 
            return render_template("register.html")
        if not confirmation:
            flash("must provide confirmation", "warning") 
            return render_template("register.html")
        if password != confirmation:
            flash("password and confirmation aren't the same", "danger") 
            return render_template("register.html")

        db = get_db()

        unique = db.execute("SELECT * FROM users WHERE username = ?",(username,)).fetchall()

        if len(unique) > 0:
            flash("username already exists", "danger")
            return render_template("register.html")

        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", (username, generate_password_hash(password)))
            db.commit()
        except Exception:
            flash("username already exists", "danger")
            return render_template("register.html")

        row = db.execute("SELECT id FROM users WHERE username = ?", (username,)).fetchone()
        session["user_id"] = row["id"]
        flash("Your account has been registered", "success")
        return redirect("/")
    else:
        return render_template("register.html")

@app.route("/remove", methods=["GET", "POST"])
@login_required
def remove():
    
    user = session["user_id"]
    db = get_db()

    if request.method == "POST":
        temp = request.form.get("action")  
        if not temp:
            flash("No team selected to remove.", "warning")
            return redirect("/remove")

        nba_id = int(temp)

        db.execute("DELETE FROM my_teams WHERE nba_id = ? AND user_id = ?",(nba_id, user))
        db.commit()

        flash("Team has been removed from your account", "success")
        return redirect("/remove")
     
    else:
        teams = db.execute( "SELECT t.id AS team_id, t.full_name, t.url FROM my_teams m JOIN nba_teams t ON t.id = m.nba_id WHERE m.user_id = ? ORDER BY t.full_name", (user,) ).fetchall()

        if len(teams) == 0:
            return render_template("remove_teams.html")
        else:
            return render_template("remove_teams.html",teams = teams)


@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    user = session["user_id"]
    db = get_db()

    if request.method == "POST":
        nba_id = request.form.get("action")
        if not nba_id:
            flash("No team selected to add.", "warning")
            return redirect("/add")

        try:
            nba_id = int(nba_id)
            db.execute("INSERT INTO my_teams (nba_id, user_id) VALUES (?, ?)",(nba_id, user))
            db.commit()
            flash("Team added to your account", "success")
        except sqlite3.IntegrityError:
            flash("You already have this team.", "info")
        return redirect("/add")

    
    search = request.args.get("q", "").strip()

    if search:
        rows = db.execute("SELECT t.id AS team_id, t.full_name, t.url, CASE WHEN m.id IS NOT NULL THEN 1 ELSE 0 END AS in_my_teams FROM nba_teams t LEFT JOIN my_teams m ON t.id = m.nba_id AND m.user_id = ? WHERE t.full_name LIKE ? COLLATE NOCASE ORDER BY t.full_name",(user, f"%{search}%")).fetchall()
    else:
        rows = db.execute("SELECT t.id AS team_id, t.full_name, t.url, CASE WHEN m.id IS NOT NULL THEN 1 ELSE 0 END AS in_my_teams FROM nba_teams t LEFT JOIN my_teams m ON t.id = m.nba_id AND m.user_id = ? ORDER BY t.full_name",(user,)).fetchall()

    return render_template("add_teams.html", teams=rows, search=search)

@app.route("/settings", methods=["GET", "POST"])
@login_required
def settings():
    return render_template("settings.html")

@app.route("/password", methods=["GET", "POST"])
@login_required
def password():

    if request.method == "POST":
        user = session["user_id"]
        db = get_db()

        old = request.form.get("old")
        new_password = request.form.get("password")
        comfirm = request.form.get("confirmation")

        users = db.execute("SELECT * FROM users WHERE id = ?",(user,)).fetchall()[0]

        if not check_password_hash(users["hash"], old):
            flash("Your old Password is Incorect ","warning")
            return render_template("password.html")
        if new_password != comfirm:
            flash("the Comfirmation and the new Password are not equal","warning")
            return render_template("password.html")
        

        db.execute("UPDATE users SET hash = ? WHERE id = ?", (generate_password_hash(new_password), user))
        flash("Password Updated","success")
        db.commit()

        return redirect("/")
    else:
        return render_template("password.html")


@app.route("/username", methods=["GET", "POST"])
@login_required
def username():
    
    if request.method == "POST":
        user = session["user_id"]
        db = get_db()

        old = request.form.get("old")
        new_username = request.form.get("username")
        comfirm = request.form.get("confirmation")

        users = db.execute("SELECT * FROM users WHERE id = ?",(user,)).fetchall()[0]

        if users["username"] != old:
            flash("Your old Username is Incorect ","warning")
            return render_template("username.html")
        if new_username != comfirm:
            flash("the Comfirmation and the new Username are not equal","warning")
            return render_template("username.html")
        
        if old == new_username:
            flash("your old Username is the same as your New one ","warning")

        db.execute("UPDATE users SET username = ? WHERE id = ?", (new_username, user))
        flash("Username Updated","success")
        db.commit()

        return redirect("/")
    else:
        return render_template("username.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)

