import requests
import hashlib
import os
from flask import Flask, Blueprint, request, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required
from database.table_definition import Users
from database.database_connection import Session

auth = Blueprint('auth', __name__)


@auth.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        try:
            email = request.form.get('InputEmail')
            password = str(request.form.get('InputPassword'))
            if len(password) < 5:
                flash("Password must be at least 5 chatacters")
                return render_template("register.html")
            salt = os.urandom(16).hex()
            password_hash = hashlib.sha256((password + salt).encode()).hexdigest()
            session = Session()

            user = session.query(Users).filter(Users.username == email).first()
            if user:
                flash("User alredy exist")
                return render_template("register.html")
            new_user = Users(username=email, password_hash=password_hash, salt=salt)
            session.add(new_user)
            session.commit()
            flash("Registration succesfull")
            login_user(user=new_user, remember=True)
            session.close()
            flash("Login Successfull")
            return redirect(url_for('main.profile'))
        except Exception as e:
            flash("Something goes wrong")
            print(e)
        
    return render_template("register.html")

@auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('InputEmail')
        password = str(request.form.get('InputPassword'))
        session = Session()
        user = session.query(Users).filter(Users.username == email).first()

        if user and user.password_hash == hashlib.sha256((password + user.salt).encode()).hexdigest():
            login_user(user=user, remember=True)
            flash("Login Successfull")
            return redirect(url_for('main.profile'))
        else:
            flash("Wrong data")


    return render_template("login.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))