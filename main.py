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
        return "<h2>Too high! Try again.</h2>"
    elif number < secret_number:
        return "<h2>Too low! Try again.</h2>"
    else:
        return "<h2>Correct! You won.</h2>"


if __name__ == "__main__":
    app.run(debug=True)
