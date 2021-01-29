from flask import Flask, render_template, request
app= Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def recieve_data():
    name = request.form["username"]
    password = request.form["password"]
    return f"<h1>Name: {name}</h1><h1>Password: {password}</h1>"

# can accept multiple parameters like this
# @app.route("/contact", methods=["GET", "POST"]

if __name__ == '__main__':
    app.run(debug=True)