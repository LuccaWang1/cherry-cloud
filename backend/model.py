"""Models for cherry-cloud app."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


#USER STORIES: 
#A user can have many posts, but a post will only have one user. User-Post is a one-to-many relationship between tables.
#A user can have many feedback comments, but a feedback comment will only have one user. User-Feedback is a one-to-many relationship between tables.
#A user can add many cherries in their cart in session, but a cherry only has one user. User-Cherry is a one-to-many relationship between tables. Notes: use conditional rendering to tell the user if what's in their cart is not longer in stock with a flash message - and also on the products page with a background color nothing or white with color font "out of stock", possible: watched by x users.


class User(db.Model): 
    """Cherry Cloud user/customer."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(25), nullable=False)
    user_email = db.Column(db.String(40), unique=True, nullable=False)
    user_password = db.Column(db.String(10), unique=True, nullable=False) 

    #posts = db.relationship("Post", back_populates="users") 

    def __init__(self, username, user_email, user_password):
        self.username = username 
        self.user_email = user_email
        self.user_password = user_password #add in hashing later 
    
    def __repr__(self):
        """Convenience method to show information about user/customer in console."""

        return f"<User: {self.username}, {self.user_email}>"

class Post(db.Model):
    """A review, like a blog post."""

    __tablename__ = "posts"

    post_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(25), nullable=False)
    body = db.Column(db.Text, nullable=False)

    users = db.relationship("User", back_populates="posts") #add secondary if many to many relationship - thinking yes 

    def __init__(self, title, body):
        self.title = title 
        self.body = body

    def __repr__(self):
        """Convenient method to show information about user feedback in console"""
        
        return f"<Post: {self.post_id}, {self.title}>"

class Feedback(db.Model):
    """A user can submit a feedback comment to app creators - will be saved in the database to be manually checked by creators and fixed."""

    __tablename__ = "feedback"

    feedback_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    feedback_body = db.Column(db.Text, nullable=False)

    users = db.relationship("User", back_populates="feedback") #add secondary if many to many relationship - thinking yes 

    def __init__(self, body):
        self.feedback_body = body


    def __repr__(self):
        return f"<Post: {self.feedback_id}, {self.feedback_body}>"
    
    
class Cherry(db.Model):
    """A cherry instance, used in the shopping cart products."""

    __tablename__ = "cherries"

    cherry_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cherry_type = db.Column(db.String(50), nullable=False) #bunch, pair, single
    price = db.Column(db.Float, nullable=False) #10, 4, 2
    image_url = db.Column(db.String(200), nullable=False)

    def __init__(self, cherry_type, price, image_url):
        self.cherry_type = cherry_type 
        self.price = price 
        self.image_url = image_url 

    def __repr__(self):
        return f"<Cherry: {self.cherry_type}, {self.price}>"

def connect_to_db(flask_app, db_uri="postgresql:///cherry-cloud", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from backend.server import app
    
    connect_to_db(app)

    with app.app_context():
        db.create_all()