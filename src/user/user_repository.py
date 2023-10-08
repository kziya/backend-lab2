from src.user.user_entity import User


class UserRepository:
    _users = []

    def addUser(self, name):
        if not self._users:
            user = User(1, name).getDict()
            self._users.append(user)
        else:
            lastElemId = self._users[-1].get('id')
            user = User(lastElemId + 1, name).getDict()
            self._users.append(user)
            return user

    def removeUserById(self, id):
        targetUserIndex = self._getIndexById(id)
        if targetUserIndex is not None:
            self._users.pop(targetUserIndex)
            return True
        else:
            return False

    def getAllUsers(self):
        return self._users

    def getUserById(self, id):
        targetUserIndex = self._getIndexById(id)
        if targetUserIndex is not None:
            return self._users[targetUserIndex]
        else:
            return None

    def _getIndexById(self, id):
        targetUserIndex = None
        for index, user in enumerate(self._users):
            if user.get('id') == id:
                targetUserIndex = index
                break
        return targetUserIndex


userRepository = UserRepository()
