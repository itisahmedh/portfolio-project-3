import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env"):
    import env

app = Flask(__name__) 
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")       
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URI")  

db = SQLAlchemy(app)


from gameshub import routes


