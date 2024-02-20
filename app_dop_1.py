from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'stephand'


class ImageForm(FlaskForm):
    image = FileField(validators=[
        FileRequired(),
        FileAllowed(['png', 'jpg', 'jpeg'], 'This file is not a valid image!')
    ])
    submit = SubmitField('submit', validators=[])


@app.route('/<title>')
def base(title: str):
    params = {
        'title': title,
    }
    return render_template('base1.html', **params)


@app.route('/galery', methods=['GET', 'POST'])
def galery():
    form = ImageForm()

    if form.validate_on_submit():
        f = request.files['image']
        f.save(os.path.join('./static/uploads', f.filename))

    image = ['./static/uploads/' + el for el in os.listdir('./static/uploads')]
    print(image)
    params = {
        'form': form,
        'images': image
    }
    return render_template('gallery.html', **params)


if __name__ == '__main__':
    app.run()
