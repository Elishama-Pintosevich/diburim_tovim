from google.cloud import texttospeech
from google.oauth2 import service_account
import json
import os
from dotenv import load_dotenv




def get_credentials_from_json_env():
    load_dotenv()
    json_str = os.environ['FILE']
    if not json_str:
        raise EnvironmentError("The GOOGLE_CLOUD_CREDENTIALS_JSON environment variable is not set or is empty")

    service_account_info = json.loads(json_str)
    
    credentials = service_account.Credentials.from_service_account_info(service_account_info)
    return credentials



def get_speech_from_text(text):

    credentials = get_credentials_from_json_env()

    client = texttospeech.TextToSpeechClient(credentials=credentials)

    synthesis_input = texttospeech.SynthesisInput(text=text)
  
    voice = texttospeech.VoiceSelectionParams(
        language_code="he-IL",name="he-IL-Standard-C", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    
    )
    return response.audio_content

