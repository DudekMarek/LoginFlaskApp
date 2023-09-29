import requests
from flask import Flask, Blueprint, request, render_template

views = Blueprint('views', __name__)

@views.route('/', methods = ['GET'])
def home():
        
    return render_template("home.html")
