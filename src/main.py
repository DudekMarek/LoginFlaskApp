from flask import Flask

app = Flask(__name__)

from views import views

app.register_blueprint(views)

app.run(host="0.0.0.0", debug=False)
