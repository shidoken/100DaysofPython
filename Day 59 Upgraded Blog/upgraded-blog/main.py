from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)

posts = requests.get('https://api.npoint.io/43644ec4f0013682fc0d').json()

MY_EMAIL = 'email here'
MY_PASSWORD = 'password here'

@app.route("/")
def index():
    return render_template('index.html', all_posts=posts)


@app.route("/post/<num>")
def post(num):
    num1 = int(num)
    return render_template('post.html', num=num1, all_posts=posts)


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/form-entry", methods=["POST", "GET"])
def receive_data():
    if request.method == "POST":
        data = request.form
        name = data["name"]
        email = data["email"]
        phone = data["phone"]
        message = data["message"]
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs='shidoken@gmail.com',
            msg=f"Subject:New email from {name}: {phone}\n\nThis email is from {name}.\nEmail: {email}\nPhone:{phone}\nMessage: {message}")
        return render_template("contact.html", value=True)
    return render_template("contact.html", value=False)


if __name__ == "__main__":
    app.run(debug=True)