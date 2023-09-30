from flask import Flask
from flask_login import LoginManager
from auth import auth
from main import main
from database.database_connection import Session
from database.table_definition import Users

app = Flask(__name__)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    session = Session()
    user = session.query(Users).filter(Users.user_id == user_id).first()
    return user

app.register_blueprint(main)
app.register_blueprint(auth)

app.secret_key="super_secret"

app.run(host="0.0.0.0", debug=True)
