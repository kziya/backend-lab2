from flask import jsonify

from src.category.category_repository import CategoryRepository

categoryRepository = CategoryRepository()


class CategoryService:
    def addCategory(self, requestBody):
        categoryName = requestBody.get('name')
        if categoryName is None:
            return jsonify({'message': 'Bad request'}), 400

        addResult = categoryRepository.addCategory(categoryName)
        return jsonify({'result': addResult}), 201

    def getAllCategories(self):
        return jsonify(categoryRepository.getAllCategories()), 200

    def deleteCategory(self, requestBody):
        categoryId = requestBody.get('id')
        if categoryId is None:
            return jsonify({'message': 'Bad request'}), 400

        removeResult = categoryRepository.removeCategoryById(categoryId)
        if not removeResult:
            return jsonify({'message': 'Category is not found !'}), 404
        return {'result': removeResult}, 200
