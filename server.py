"""Server for cloud-cherry app."""

import os
from jinja2 import StrictUndefined
from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db, User, Post, Feedback, Cherry, Cherry_Cart, Cart
import json
import crud

app = Flask(__name__, static_folder='static',
            static_url_path='/static')

# app.secret_key = os.environ["KEY"]
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """View homepage."""

    return render_template("homepage.html")


@app.route("/cherries")
def cherries():
    """View cherries."""

    return render_template("cherries.html")


@app.route("/reviews")
def reviews():
    """View reviews by cherries."""

    all_posts = crud.retrieve_all_posts()

    return render_template("reviews.html", posts=all_posts)


@app.route("/my-account")
def my_account():
    """View my account and settings."""

    return render_template("my_account.html")


@app.route("/cart")
def cart():
    """View cart."""

    return render_template("cart.html")


if __name__ == "__main__":
    connect_to_db(app)

    app.run(host="0.0.0.0", debug=True)
