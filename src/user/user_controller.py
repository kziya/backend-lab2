from flask import request

from src import app
from src.user.user_service import UserService

userService = UserService()


@app.route('/user/<int:id>', methods=['GET'])
def getUserById(id):
    return userService.getUserById(id)


@app.route('/user', methods=['POST'])
def addUser():
    return userService.addUser(request.get_json())


@app.route('/users', methods=['GET'])
def getUsers():
    return userService.getUsers()


@app.route('/user/<int:id>', methods=['DELETE'])
def deleteUser(id):
    return userService.deleteUser(id)
