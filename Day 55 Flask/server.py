from flask import Flask
import random

random_number = random.randint(0, 9)

app = Flask(__name__)


@app.route("/")
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route("/<int:guess>")
def guessing_number(guess):
    if guess < random_number:
        return '<h1 style=red>Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/IevhwxTcTgNlaaim73/giphy.gif">'
    elif guess > random_number:
        return '<h1 style=red>Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/VkIet63SWUJa0/giphy.gif">'
    else:
        return '<h1 style=red>You got it right!</h1>' \
               '<img src="https://media.giphy.com/media/sv7SJhzniNUWs/giphy.gif">'


if __name__ == "__main__":
    # run the app in debug mode
    app.run(debug=True)