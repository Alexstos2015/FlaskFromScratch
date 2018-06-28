from flask import Flask,render_template, flash, redirect, url_for, session, logging
from data import Articles
from flask_sqlalchemy import *
from  wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt


app = Flask(__name__)

Articles = Articles()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)

@app.route('/articles/<string:id>')
def article(id):
    return render_template('article.html', id=id)



class RegisterForm(Form):
    name = StringField('Name',[validators.length(min=3,max=50)])
    username = StringField('UserName',[validators.Length(min=4,max=25)])
    email = StringField('Email',[validators.Length(min=6,max=50)])
    password = PasswordField('Password',[
        validators.DataRequired(),
        validators.EqualTo('confirm', message="Пароли не совпадают")
    ])
    confirm = PasswordField('Confirm Password')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)

if __name__ == '__main__':
    app.run(debug=True)
