from flask import Flask
from random import randint

app = Flask(__name__)

secret_number = randint(0, 100)


@app.route("/")
def home():
    return """<h2>Guess a number between 0 and 100</h2>
    <p>Type it in the address bar after a slash ('/') symbol</p>
    <img src = 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='gif'/> """


@app.route("/<int:number>")
def check_number(number):
    if number > secret_number:
        return """<h2 style='color:red'>Too high! Try again.</h2>
        <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"""
    elif number < secret_number:
        return """<h2 style='color:red'>Too low! Try again.</h2>
        <img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"""
    else:
        return """<h2 style='color:green'>Correct! You won.</h2>
        <img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"""


if __name__ == "__main__":
    app.run(debug=True)
