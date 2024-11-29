from database import db

class User(db.Model):
        id = db.Column(db.Interger, primary_key = True)
        titulo = db.Column(db.String(200))
        conteudo = db.Column(db.Text)
        user_id = db.Column(db.Interger, db.ForeignKey("user.id"))

    def toJson(self):
        return{"id": self.id,"nome": self.nome,"email": self.email }
        