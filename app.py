from flask import Flask, render_template, request, redirect, url_for, session, jsonify, send_file
import sqlite3, os, json
from datetime import datetime, date
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import io

app = Flask(__name__)
app.secret_key = "genesys-pottery-secret-2024"
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def get_db():
    conn = sqlite3.connect("pottery.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            streak INTEGER DEFAULT 0,
            last_checkin TEXT
        );
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            image TEXT NOT NULL,
            tags TEXT DEFAULT '',
            likes INTEGER DEFAULT 0,
            user_id INTEGER
        );
        CREATE TABLE IF NOT EXISTS likes (
            user_id INTEGER,
            product_id INTEGER,
            PRIMARY KEY (user_id, product_id)
        );
    """)
    # Seed some products if empty
    cur = conn.execute("SELECT COUNT(*) FROM products")
    if cur.fetchone()[0] == 0:
        seeds = [
            ("Small Pots", "small_pots.jpg", "#handmade, #clay, #decor"),
            ("Long Pot", "long_pot.jpg", "#minimal, #long, #porcelain"),
            ("Glazed Pot", "glazed_pot.jpg", "#glazed, #shiny, #artsy"),
            ("Unique Pot", "unique_pots.jpg", "#unique, #bold, #modern"),
            ("Plant Holder", "plant_holder.jpg", "#green, #nature, #home"),
            ("Designs", "designs.jpg", "#artistic, #pattern, #craft"),
            ("Clay Mug", "clay_mug.jpg", "#mug, #earthy, #handcrafted"),
        ]
        conn.executemany("INSERT INTO products (name, image, tags) VALUES (?,?,?)", seeds)
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        conn = get_db()
        user = conn.execute("SELECT * FROM users WHERE email=?", (email,)).fetchone()
        conn.close()
        if user and check_password_hash(user["password"], password):
            session["user_id"] = user["id"]
            session["user_name"] = user["name"]
            # Check streak
            today = str(date.today())
            conn = get_db()
            if user["last_checkin"] != today:
                from datetime import timedelta
                yesterday = str(date.today() - timedelta(days=1))
                new_streak = (user["streak"] + 1) if user["last_checkin"] == yesterday else 1
                conn.execute("UPDATE users SET streak=?, last_checkin=? WHERE id=?",
                             (new_streak, today, user["id"]))
                conn.commit()
                session["streak"] = new_streak
            else:
                session["streak"] = user["streak"]
            conn.close()
            return redirect(url_for("marketplace"))
        return render_template("login.html", error="Invalid email or password")
    return render_template("login.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = generate_password_hash(request.form["password"])
        try:
            conn = get_db()
            conn.execute("INSERT INTO users (name, email, password) VALUES (?,?,?)", (name, email, password))
            conn.commit()
            conn.close()
            return redirect(url_for("login"))
        except:
            return render_template("register.html", error="Email already registered")
    return render_template("register.html")

@app.route("/marketplace")
def marketplace():
    if "user_id" not in session:
        return redirect(url_for("login"))
    conn = get_db()
    products = conn.execute("SELECT * FROM products").fetchall()
    liked = [r["product_id"] for r in conn.execute(
        "SELECT product_id FROM likes WHERE user_id=?", (session["user_id"],)).fetchall()]
    conn.close()
    return render_template("marketplace.html", products=products, liked=liked,
                           streak=session.get("streak", 0))

@app.route("/like/<int:pid>", methods=["POST"])
def like(pid):
    if "user_id" not in session:
        return jsonify({"error": "not logged in"}), 401
    uid = session["user_id"]
    conn = get_db()
    existing = conn.execute("SELECT * FROM likes WHERE user_id=? AND product_id=?", (uid, pid)).fetchone()
    if existing:
        conn.execute("DELETE FROM likes WHERE user_id=? AND product_id=?", (uid, pid))
        conn.execute("UPDATE products SET likes=likes-1 WHERE id=?", (pid,))
        liked = False
    else:
        conn.execute("INSERT INTO likes VALUES (?,?)", (uid, pid))
        conn.execute("UPDATE products SET likes=likes+1 WHERE id=?", (pid,))
        liked = True
    conn.commit()
    likes = conn.execute("SELECT likes FROM products WHERE id=?", (pid,)).fetchone()["likes"]
    conn.close()
    return jsonify({"liked": liked, "likes": likes})

@app.route("/streak")
def streak():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("streak.html", name=session["user_name"], streak=session.get("streak", 0))

@app.route("/certificate")
def certificate():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("certificate.html", name=session["user_name"], streak=session.get("streak", 0))

@app.route("/sell", methods=["GET","POST"])
def sell():
    if "user_id" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        name = request.form["name"]
        file = request.files["image"]
        if file and name:
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            conn = get_db()
            conn.execute("INSERT INTO products (name, image, user_id) VALUES (?,?,?)",
                         (name, filename, session["user_id"]))
            conn.commit()
            conn.close()
            return redirect(url_for("marketplace"))
    return render_template("sell.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
