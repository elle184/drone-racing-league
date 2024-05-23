from ..dao.user_dao import UserDao

class UserService :

    def getById(self, id):
        user_dao = UserDao()

        return user_dao.findById(id)