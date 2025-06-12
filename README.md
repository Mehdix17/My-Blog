# 📰 My-Blog

A minimal, responsive blog web application built with **Flask**, styled with **Bootstrap**, and deployed on **Vercel**. Users can read posts, submit a contact form, and explore articles rendered dynamically from JSON or a backend source.

---

## 🚀 Features

- 🧠 Flask-powered server-side rendering
- ✍️ Jinja2 templating with reusable components (`header.html`, `footer.html`)
- 📬 Contact form with email delivery via `smtplib`
- 📸 Posts with dynamic image backgrounds (Unsplash)
- 🧾 Blog content driven by structured JSON
- ☁️ Deployed on [Vercel](https://vercel.com/)

---

## 📁 Project Structure

My-Blog/ \
│ \
├── api/ or main.py # Flask application entry point \
├── templates/ # Jinja2 HTML templates \
│ ├── header.html \
│ ├── footer.html \
│ └── post.html \
├── static/ # CSS, JS, images \
├── vercel.json # Vercel deployment config \
├── .gitignore # Ignored files \
├── requirements.txt # Python dependencies \
└── README.md # You are here \
