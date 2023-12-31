from flask import jsonify

from src.category.category_repository import categoryRepository


class CategoryService:
    def addCategory(self, requestBody):
        categoryName = requestBody.get('name')
        if categoryName is None:
            return jsonify({'message': 'Bad request'}), 400

        addResult = categoryRepository.addCategory(categoryName)
        return jsonify(addResult), 201

    def getAllCategories(self):
        return jsonify(categoryRepository.getAllCategories()), 200

    def deleteCategory(self, id):
        if id is None:
            return jsonify({'message': 'Bad request'}), 400

        removeResult = categoryRepository.removeCategoryById(id)
        if not removeResult:
            return jsonify({'message': 'Category is not found !'}), 404
        return {'result': removeResult}, 200
