from pycket import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import enum

class ticket_statuses(enum.Enum):
    one = "Open"
    two = "Requested Information From User"
    three = "Resolved"
    four = "Closed"
    five = "Duplicate"
    six = "Archived"

class product_category(enum.Enum):
    one = "Chromebook"
    Two = "Keyboard"
    Three = "Mice"
    Four = "Headset/Mic"
    Five = "Software"

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), index=True, unique=True)
    firstname = db.Column(db.String(64), index=True)
    lastname = db.Column(db.String(64), index=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.email)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64), index=True)
    lastname = db.Column(db.String(64), index=True)
    phone_number = db.Column(db.String(10), index=True)
    email = db.Column(db.String(128), index=True)
    location = db.Column(db.String(200), index=True)
    subject = db.Column(db.String(140), index=True)
    description = db.Column(db.String(1000))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    status = db.Column(db.String(35), default=ticket_statuses.one)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def set_firstname(self, firstname):
        self.firstname = firstname

    def set_lastname(self, lastname):
        self.lastname = lastname
    
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_location(self, location):
        self.location = location

    def set_subject(self, subject):
        self.subject = subject

    def set_description(self, description):
        self.description = description
    
    def set_status(self, status):
        self.status = status
    
    def get_id(self):
        return self.id

    def get_creation_timestamp(self):
        return self.timestamp

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.last_name

    def get_phone_number(self):
        return self.phone_number

    def get_location(self):
        return self.location

    def get_subject(self):
        return self.subject

    def get_description(self):
        return self.description
    
    def get_status(self):
        return self.status

    def __repr__(self):
        return '<Ticket {}>'.format(self.body)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(64), index=True, primary_key=True)
    price = db.Column(db.String(64), index=True)
    category = db.Column(db.String(12), index=True)
    description = db.Column(db.String(500))