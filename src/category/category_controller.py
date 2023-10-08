from flask import request

from src import app
from src.category.category_service import CategoryService

categoryService = CategoryService()


@app.route('/category', methods=['POST'])
def addCategory():
    return categoryService.addCategory(request.get_json())


@app.route('/category', methods=['GET'])
def getCategories():
    return categoryService.getAllCategories()


@app.route('/category', methods=['DELETE'])
def deleteCategory():
    return categoryService.deleteCategory(request.get_json())
