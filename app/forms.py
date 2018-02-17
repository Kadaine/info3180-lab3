from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from flask import Flask, render_template, flash, session, redirect, url_for

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

class Myform(FlaskForm):
    name = StringField('name', validators = [DataRequired("Your name is missing")])
    email = StringField('email', validators = [DataRequired("Your email is required"), Email()])
    subject =StringField('subject', validators = [DataRequired("Message subject is required")])
    message = TextAreaField('message', validators = [DataRequired("Message is required")])
    button = SubmitField('Send')