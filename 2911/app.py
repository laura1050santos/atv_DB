from flask import Flask
from database import init_db
from controller import userController

app= Flask(__name__)
app.register_blueprint(userController)
lstjson=[]


init_db(app)


if __name__  == "__main__":  
    app.run(debug=True)