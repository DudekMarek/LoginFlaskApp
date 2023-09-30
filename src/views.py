import requests
import hashlib
import os
from flask import Flask, Blueprint, request, render_template, flash
from database.table_definition import Users
from database.database_connection import Session

views = Blueprint('views', __name__)

@views.route('/', methods = ['GET'])
def home():
        
    return render_template("home.html")

@views.route('/register', methods=["GET", "POST"])
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
            new_user = Users(username=email, password_hash=password_hash, salt=salt)
            
            session = Session()
            session.add(new_user)
            session.commit()
            session.close()
            flash("Registration succesfull")
        except Exception as e:
            flash("Something goes wrong")
            print(e)
        
    return render_template("register.html")

@views.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('InputEmail')
        password = str(request.form.get('InputPassword'))
        session = Session()
        record = session.query(Users).filter(Users.username == email).first()

        if record and record.password_hash == hashlib.sha256((password + record.salt).encode()).hexdigest():
            flash("Login Successfull")
            return render_template("home.html")
        else:
            flash("Wrong data")


    return render_template("login.html")