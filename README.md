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
├── app.py                  
├── pottery.db              
├── requirements.txt        
├── static/
│   ├── images/             
│   └── uploads/            
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

Python + Flask
SQLite
HTML, CSS, JavaScript
Werkzeug for password hashing

---

## ☁️ Deployment (Free)

This needs a Python backend so it won't work on GitHub Pages. I'd recommend deploying on Render.com — it's free and works great with Flask.

---

<p align="center">Made with ❤️ and clay 🏺</p>