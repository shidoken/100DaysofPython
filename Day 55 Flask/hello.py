from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"
    return wrapper_function


@app.route("/")
def hello_world():
    return 'Hello, World!'


@app.route("/bye")
@make_bold
def bye():
    return 'Bye!'


# creating variable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there{name}, you are {number} years old!"


if __name__ == "__main__":
    # run the app in debug mode
    app.run(debug=True)
