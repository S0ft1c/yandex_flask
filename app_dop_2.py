from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
import json
from random import randint
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'stephand'


@app.route('/<title>')
def base(title: str):
    params = {
        'title': title,
    }
    return render_template('base1.html', **params)


@app.route('/member')
def member():

    with open('./templates/ppl.json') as ppl:
        data = ppl.read()
        data = json.loads(data)
    rnd = randint(0, len(data) - 1)
    data = data[rnd]
    params = {
        'h1': data['name'],
        'image': data['image'],
        'desc': data['desc'],
    }
    return render_template('member.html', **params)


if __name__ == '__main__':
    app.run()
