from flask import Flask, render_template, redirect, request
from login_form import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'stephand'


@app.route('/<title>')
def base(title: str):
    params = {
        'title': title,
    }
    return render_template('base1.html', **params)


if __name__ == '__main__':
    app.run()
