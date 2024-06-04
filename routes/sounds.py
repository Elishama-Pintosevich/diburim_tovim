from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from models import SoundModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from schemas import SoundSchema, SoundBaseSchema
from services import get_speech_from_text
from services import upload_file, create_file, delete_file
import uuid


blp = Blueprint("sounds", __name__, description = "sounds controller")


@blp.route("/sounds")   
class Actions(MethodView):
    @blp.response(200, SoundSchema(many=True))
    def get(self):
        return SoundModel.query.all()
    
    @blp.arguments(SoundSchema)
    @blp.response(201, SoundSchema)
    def post(self, user_data):
        
        random_uuid = uuid.uuid4()
        hex_string = random_uuid.hex[:6]
        file_name = f'{user_data['type']}_{hex_string}_{user_data['action_id']}.mp3'

        user_data['path'] = f'{user_data['bpn']}/{file_name}'
        mp_3 = get_speech_from_text(user_data['content'])

        # create_file(mp_3, f"tmp_files/{file_name}")
        upload_file("sound-storage", mp_3, user_data['path'])
        # delete_file(f"tmp_files/{file_name}")

        store = SoundModel(**user_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(400, message="same phone number exist")    
        except SQLAlchemyError:
            abort(500, message="an error occured while inserting action")

        return store 