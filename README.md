# 💼 Streamlit x FastAPI Expense Tracker

A clean, full-stack personal finance tracker that uses **FastAPI for backend** and **Streamlit for frontend** to deliver real-time expense entry, visualizations, and modular API design.

This project was built in one night to showcase:
- ✅ End-to-end FastAPI skills (routing, models, CORS, SQLAlchemy)
- ✅ Modular backend/frontend separation
- ✅ Live frontend powered by Streamlit + Plotly
- ✅ Clean OpenAPI documentation at `/docs`

---

## 🚀 Features

- Add and view categorized expenses
- Real-time pie chart showing where your money is going
- Built using Python, FastAPI, and Streamlit
- Simple SQLite backend via SQLAlchemy ORM
- OpenAPI Docs for all endpoints (FastAPI magic!)

---

## 🧠 Why “Smart”?
While this version doesn't include deep AI yet, the app is built to:
- Be **AI-ready** (you can plug in a model for category prediction or analysis)
- Showcase clean, scalable architecture for smart apps
- Deliver real-time interactivity

---

## 🔧 Run Locally

### 1. Clone and set up environment
```bash
git clone https://github.com/your-username/expense-tracker.git
cd ai_expense_tracker
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run backend
```bash
uvicorn backend.main:app --reload
```

Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 3. Run frontend
```bash
cd frontend
streamlit run app.py
```

---

## 📦 Tech Stack

- **FastAPI** – blazing-fast backend API framework
- **Streamlit** – reactive Python frontend
- **SQLAlchemy** – ORM for SQLite
- **Plotly** – for data visualization

---

## 📌 Future Improvements
- 🤖 AI-powered category suggestions
- 🔔 Budget alerts and summaries
- 📅 Date filtering and weekly reports
