from dao import UserDao

class UserRepository:
    def __init__(self):
        self.userDAO = UserDao()

    def buscar_todos_usuario_json(self):
        users= self.userDAO.buscar_tds_usuarios()
        listaJson = []
        for user in users:   
            listaJson.append(user.toJson())
        return listaJson
    
    def add(self):
        retorno= UserDao.add("laura", "lauraGarden@10.com")
        if retorno:
            return "adicionado com sucesso"
        return "erro ao adicionar"