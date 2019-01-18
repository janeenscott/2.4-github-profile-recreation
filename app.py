import csv

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)




@app.route("/")
def index():
    user_data = requests.get(https://api.github.com/users/<username>)
    translated = user_data.json()

    context = {
        'name': translated['name'],
        'username':translated['login']
        'bio': translated['bio'],
        'location': translated['location'],
        'email': translated['email'],
        'avatar_url': translated['avatar_url'],
        'repos_url': translated['repos_url']
    }

    return render_template('index.html', **context)

