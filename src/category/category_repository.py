from src.category.category_entity import Category


class CategoryRepository:
    _categories = []

    def addCategory(self, name):
        if not self._categories:
            self._categories.append(Category(1, name).getDict())
        else:
            lastElemId = self._categories[-1].get('id')
            self._categories.append(Category(lastElemId + 1, name).getDict())
        return True

    def removeCategoryById(self, id):
        targetCategoryIndex = self._getIndexByCategoryId(id)
        if targetCategoryIndex is not None:
            self._categories.pop(targetCategoryIndex)
            return True
        else:
            return False

    def getAllCategories(self):
        return self._categories

    def getCategoryById(self, id):
        targetCategoryIndex = self._getIndexByCategoryId(id)
        if targetCategoryIndex is not None:
            return self._categories[targetCategoryIndex]
        else:
            return None

    def _getIndexByCategoryId(self, id):
        targetCategoryIndex = None
        for index, category in enumerate(self._categories):
            if category.get('id') == id:
                targetCategoryIndex = index
                break
        print(id, targetCategoryIndex)
        return targetCategoryIndex
