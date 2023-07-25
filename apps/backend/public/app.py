from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from dimecom.apps.backend.config.routes.routes import Routes

import os
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("DATABASE_SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'mysql://'
    f'{os.getenv("DATABASE_USER")}:{os.getenv("DATABASE_PASSWORD")}'
    f'@{os.getenv("DATABASE_HOST")}:{os.getenv("DATABASE_PORT")}/{os.getenv("DATABASE_NAME")}'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv("DATABASE_TRACK_MODIFICATIONS")

db  = SQLAlchemy(app)
api = Api(app)

routes = Routes(api, db)
routes.initializeRoutes()



if __name__ == '__main__':
    app.run(port=5000, debug=True)