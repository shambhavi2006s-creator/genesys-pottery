# 🏺 Genesys School of Pottery

> A full-stack web app for a pottery school — browse handcrafted pieces, track your daily streak, earn certificates, and sell your own creations.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-black?style=flat-square&logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightblue?style=flat-square&logo=sqlite)

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔐 Auth | Register & login with hashed passwords |
| 🛒 Marketplace | Browse pottery products, like your favourites |
| 🔥 Streak Tracker | Log in daily to build your streak |
| 🏆 Certificate | Unlock a downloadable certificate after a 7-day streak |
| 📦 Sell | Upload and list your own pottery pieces |

---

## 📸 Preview

> _Add screenshots here after deployment_

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/genesys-pottery.git
   cd genesys-pottery
   ```

2. **Create a virtual environment** _(recommended)_
   ```bash
   python -m venv venv
   source venv/bin/activate       # macOS/Linux
   venv\Scripts\activate          # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   python app.py
   ```

5. **Open in browser**
   ```
   http://localhost:5000
   ```

---

## 🗂️ Project Structure

```
genesys-pottery/
├── app.py                  # Main Flask application
├── pottery.db              # SQLite database (auto-created)
├── requirements.txt        # Python dependencies
├── static/
│   ├── images/             # Product images
│   └── uploads/            # User-uploaded pottery images
└── templates/
    ├── base.html
    ├── login.html
    ├── register.html
    ├── marketplace.html
    ├── streak.html
    ├── certificate.html
    └── sell.html
```

---

## 🛠️ Tech Stack

- **Backend** — Python + Flask
- **Database** — SQLite (via `sqlite3`)
- **Frontend** — HTML, CSS, JavaScript (vanilla)
- **Auth** — Werkzeug password hashing
- **Fonts** — Playfair Display (Google Fonts)

---

## 📦 requirements.txt

Make sure your `requirements.txt` includes:
```
flask
werkzeug
```

Generate it automatically with:
```bash
pip freeze > requirements.txt
```

---

## ☁️ Deployment (Free)

This app needs a Python backend, so it **cannot** run on GitHub Pages.

### Deploy on [Render.com](https://render.com) (recommended — free tier)

1. Push your code to GitHub
2. Go to [render.com](https://render.com) → **New Web Service**
3. Connect your GitHub repo
4. Set:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Click **Deploy** 🎉

> Don't forget to add `gunicorn` to your `requirements.txt` before deploying.

---

## 🔒 Environment Variables

For production, replace the hardcoded secret key in `app.py`:

```python
app.secret_key = os.environ.get("SECRET_KEY", "fallback-dev-key")
```

Set `SECRET_KEY` as an environment variable on your hosting platform.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

1. Fork the repo
2. Create your branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -m "Add your feature"`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request

---

<p align="center">Made with ❤️ and clay 🏺</p>