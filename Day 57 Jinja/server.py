from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    this_year = datetime.datetime.now().year
    return render_template('index.html', num=random_number, year=this_year)


@app.route("/guess/<some_name>")
def guess(some_name):
    params = {"name": some_name}
    gen_resp = requests.get("https://api.genderize.io", params)
    gresult = gen_resp.json()
    gender = gresult["gender"]
    age_resp = requests.get("https://api.agify.io", params)
    aresult = age_resp.json()
    age = aresult["age"]
    return render_template('guess.html', name=some_name.title(), gender=gender, age=age)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url="https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)

