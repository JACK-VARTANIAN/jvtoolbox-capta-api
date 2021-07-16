import os
from flask import Flask
from app.config.database import db_session
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()