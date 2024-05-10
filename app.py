from flask import Flask , request
from flask_smorest import Api
from routes.ivr import blp as IvrBlueprint
from flask_cors import CORS
import os
from twilio.rest import Client

def create_app():
    app = Flask(__name__)

    CORS(app)

    account_sid = os.environ['ACCOUNT_SID']
    auth_token = os.environ['TOKEN_SID']
    client = Client(account_sid, auth_token)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Diburim tovim - IVR, REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.1.0"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.10.0/"
    

    

    api = Api(app)
    api.register_blueprint(IvrBlueprint)

    return app

if __name__ == '__main__':
    create_app().run()









