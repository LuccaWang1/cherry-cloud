# NOT SURE WHERE TO PUT EXACTLY

"""CRUD operations."""

from model import db, User, Post, Feedback, Cherry, Cherry_Cart, Cart, connect_to_db
from sqlalchemy import update, and_

def retrieve_all_posts():
    "return all posts"

    return Post.query.all()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)