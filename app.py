"""Blogly application."""

from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'abcde'
debug=DebugToolbarExtension(app)

app.app_context().push()
app.app_context()

connect_db(app)
db.create_all()

@app.route('/')
def home():
    """home page."""
    return redirect('/users')


@app.route('/users')
def show_users():
    """List users."""
    users = User.query.all()
    return render_template("user_list.html", users=users)


@app.route("/users/new", methods=["GET"])
def new_user_form():
    """show add user form."""

    return render_template("create_user.html")


@app.route("/users/new", methods=["POST"])
def add_user():
    """Add user and redirect to list."""

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url'] or None
   

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')


@app.route("/users/<int:user_id>")
def show_user(user_id):
    """Show info on a single user."""

    user = User.query.get_or_404(user_id)

    return render_template("user_detail.html", user=user )


@app.route("/users/<int:user_id>/edit")
def edit_user(user_id):
    """show edit form."""

    user = User.query.get_or_404(user_id)
    return render_template('user_edit.html' , user=user)


@app.route("/users/<int:user_id>/edit" , methods=["POST"])
def update_user(user_id):
    """update the user."""

    user = User.query.get_or_404(user_id)
    user.first_name=request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.commit()
    flash("user edited!!")
    return redirect('/users')


@app.route("/users/<int:user_id>/delete" , methods=["POST"])
def delete_user(user_id):
    """delete the user."""

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash("user deleted!!")
    return redirect('/users')
