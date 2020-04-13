from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from pycket import auth, ticket, models, webstore
app.register_blueprint(auth.bp)
app.register_blueprint(ticket.bp)
app.register_blueprint(webstore.bp)
