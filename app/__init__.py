from flask import Flask
from flask_mail import Mail
app = Flask(__name__)
app.config['SECRET_KEY'] = 'My name is random'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] = '944d0169b61c8d'
app.config['MAIL_PASSWORD'] = '0b45c1b3b7ba80'
mail = Mail(app)

from app import views