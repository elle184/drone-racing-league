from ..modelos import db, User

class UserDao :

    def findById(self, id) :
        return User.query.filter(User.id == id).first()