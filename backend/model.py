"""Models for cherry-cloud app."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model): 
    """A user, a cherry!"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(25), nullable=False)
    user_email = db.Column(db.String(40), unique=True, nullable=False)  

    posts = db.relationship("Post", back_populates="users") #add secondary if many to many relationship - thinking yes 

    def __repr__(self):
        return f'<User id={self.user_id} ={self.username}>' 

class Post(db.Model):
    """A review, like a blog post."""

    __tablename__ = "posts"

    post_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(25), nullable=False)
    body = db.Column(db.Text, nullable=False)

    users = db.relationship("User", back_populates="posts") #add secondary if many to many relationship - thinking yes 

    def __repr__(self):
        return f'<Post id={self.post_id} ={self.title}>'


def connect_to_db(flask_app, db_uri="postgresql:///cherry-cloud", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app
    
    connect_to_db(app)

    with app.app_context():
        db.create_all()
