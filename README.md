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

## 📂 Folder Structure

├── frontend/
│ ├── src/
│ │ ├── components/
│ │ ├── pages/
│ │ └── App.tsx
├── backend/
│ ├── routes/
│ ├── models/
│ ├── db.py
│ └── app.py


---

## ⚙️ Setup Instructions

### 📦 Backend (Flask + MySQL)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py

Make sure MySQL is running and database is created.

Update db.py with your DB credentials.
