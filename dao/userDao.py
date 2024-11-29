from model import User,db

class UserDao:
    @staticmethod
    def buscar_tds_usuarios():
        return User.query.all()
    

    @staticmethod
    def add_usuario():
        try:
            user= User(nome= "Laura", email = "lauraGarden@gmail.com")
            db.session.add (user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return False