import os, requests, smtplib
from flask import Flask, render_template, request
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
API_URL = os.getenv("API_URL")

# Get the year for the footer
year = datetime.now().year

# Load data
response = requests.get(API_URL)
data = response.json()
posts = data["content"]

# Create app
app = Flask(__name__)

# Routes
@app.route("/")
def home():
    return render_template("index.html", posts=posts, year=year)

@app.route("/about")
def about():
    return render_template("about.html", year=year)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", year=year)
    elif request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        full_message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage:\n{message}"

        try:
            with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as connection:
                connection.starttls()
                connection.login(SENDER_EMAIL, SENDER_PASSWORD)
                connection.sendmail(
                    from_addr=SENDER_EMAIL,
                    to_addrs=RECEIVER_EMAIL,
                    msg=f"Subject: New Contact Message\n\n{full_message}"
                )
            return render_template("contact.html", year=year, success=True)
        except Exception as e:
            print(e)
            return render_template("contact.html", year=year, fail=True)        

@app.route("/post/<int:id>")
def post(id):
    post_path = f"posts/post{id}.html"
    post = posts[int(id) - 1]
    return render_template(post_path, post=post, year=year)

if __name__ == "__main__":
    app.run(debug=True)
