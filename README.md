# 🏋️‍♀️ Elevate Fitness Studio

A modern web application for managing and booking fitness programs like Yoga, Zumba, HIIT, and Strength Training — built using **Django** and **Bootstrap**.

---

## 🌟 Features

- ✅ User-friendly Home Page with modern UI
- 📅 Class Booking System with Modal Form
- 🧘‍♀️ Multiple Program Listings
- 🎯 Success Stories Section with Cards
- 📬 Contact Section with Personal & Professional Info
- 📱 Responsive Design with Bootstrap 5

---

## 💻 Technologies Used

- ⚙️ Python 3 & Django Framework
- 🎨 HTML5, CSS3, Bootstrap 5
- 💾 PostgreSQL (or SQLite)
- 🧠 JavaScript & AJAX
- 📸 Django Media for Instructor Images

---

## 📸 Screenshots

| Home Page | Booking Modal | Success Stories |
|----------|----------------|-----------------|
| ![Home](static/images/home.png) | ![Modal](static/images/upcoming programs.png) | ![Stories](static/images/success stories.png) |![Stories](static/images/contact.png) |

---

## 🚀 How to Run This Project

```bash
# Clone the repository
git clone https://github.com/Priyahari123/Fitness-Studio.git
cd Fitness-Studio

# Create virtual environment & activate
python -m venv env
source env/bin/activate  # For Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
# Fitness-Studio