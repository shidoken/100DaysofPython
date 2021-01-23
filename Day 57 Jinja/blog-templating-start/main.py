from flask import Flask, render_template
import requests

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/5abcca6f4e39b4955965").json()
post_objects = []
for post in posts:
    post_obj = [post["id"], post["title"], post["subtitle"], post["body"]]
    post_objects.append(post_obj)


@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)


@app.route('/post/<num>')
def get_blog(num):
    req_post = None
    for value in post_objects:
        if int(value[0]) == int(num):
            req_post = value
    return render_template("post.html", p=req_post)


if __name__ == "__main__":
    app.run(debug=True)
