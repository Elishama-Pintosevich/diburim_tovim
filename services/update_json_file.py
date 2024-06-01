import os
import json
from dotenv import load_dotenv

def update_json_template():
    
    credentials_path = 'config/application_default_credentials.json'
    
    
    
    
    with open(credentials_path, 'r') as template_file:
        json_data = json.load(template_file)

    load_dotenv()
    json_data['client_id'] = os.environ['CLIENT_ID']
    json_data['client_secret'] = os.environ['CLIENT_SECRET']
    json_data['quota_project_id'] = os.environ['QUOTA_PROJECT_ID']
    json_data['refresh_token'] = os.environ['REFRESH_TOKEN']
    json_data['type'] = os.environ['TYPE']
    json_data['universe_domain'] = os.environ['UNIVERSE_DOMAIN']
    
    
    with open(credentials_path, 'w') as credentials_file:
        json.dump(json_data, credentials_file)
    
    
    # os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

