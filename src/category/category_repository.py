from src.category.category_entity import Category


class CategoryRepository:
    categories = []

    def addCategory(self, name):
        if not self.categories:
            self.categories.append(Category(1, name))
        else:
            lastElemId = self.categories[-1].id
            self.categories.append(Category(lastElemId + 1, name))

    def removeCategoryById(self, id):
        targetCategoryIndex = self._getIndexByCategoryId(id)
        if targetCategoryIndex is not None:
            self.categories.pop(targetCategoryIndex)
            return True
        else:
            return False

    def getAllCategories(self):
        return self.categories

    def getCategoryById(self, id):
        targetCategoryIndex = self._getIndexByCategoryId(id)
        if targetCategoryIndex is not None:
            return self.categories[targetCategoryIndex]
        else:
            return None

    def _getIndexByCategoryId(self, id):
        targetCategoryIndex = None
        for index, category in enumerate(self.categories):
            if 'id' in category and category['id'] == id:
                targetCategoryIndex = index
                break
        return targetCategoryIndex
