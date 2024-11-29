from flask import Flask ,jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from database import db
from model import User, UserRepository
from dao import UserDao

userController = Blueprint("userController",__name__)
userRepository = UserRepository()
@userController.route("/")
def index():
    return "Olá Banco de Dados"

@userController.route("/add")
def add ():
    
    return userRepository.add()

@userController.route("/ver")
def ver ():
    users= User.query.all()
    lstjson=[]
    for user in users:
        lstjson.append(user.toJson())
    return jsonify(lstjson)
