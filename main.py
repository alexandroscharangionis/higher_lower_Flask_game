from flask import Flask
from random import randint

app = Flask(__name__)

secret_number = randint(0, 100)
