# 🎉 Event Tracker System

A full-stack web application that allows university students to explore, register for, and track upcoming events. It also includes club subscription features and a personalized dashboard. Built using **React**, **Flask**, and **MySQL**, the system showcases core database and backend concepts including **PL/SQL triggers and procedures**.

---

## 🚀 Features

- 🏫 View all upcoming university events
- 📝 Register for events with a single click
- 👤 User dashboard to view registered events
- 🧠 Club subscription system with notifications
- 🔔 Real-time notifications via PL/SQL trigger
- 💡 Built-in stored procedures and relational DB design

---

## 🛠️ Tech Stack

- **Frontend**: React + TypeScript + Tailwind CSS
- **Backend**: Python + Flask + Flask Blueprints
- **Database**: MySQL (with PL/SQL triggers, procedures)
- **Other**: REST APIs, PyMySQL, Vite, CORS
---

## ⚙️ Setup Instructions

### 📦 Backend (Flask + MySQL)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
```

Make sure MySQL is running and database is created.

Update db.py with your DB credentials.

### 💻 Frontend (React + Vite)
```bash
cd frontend
npm install
npm run dev
```
### 🧠 PL/SQL Concepts Demonstrated
✅ Stored Procedure: Fetch user’s registered events

✅ Trigger: Add notification when a new event is created for a subscribed club

✅ Joins, Views, Foreign Keys, etc.

### 📌 Future Enhancements
✅ Add login/signup with JWT

✅ Admin panel for event & club management

✅ Email or push notifications

✅ Real-time updates via WebSockets or polling

✅ Deployed version using Render + Vercel

# 👩‍💻 Author
Anushka SIngh
Student @ MIT WPU
[GitHub Profile](https://github.com/nush2701)




