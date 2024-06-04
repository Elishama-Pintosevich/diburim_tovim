import os
import json
from dotenv import load_dotenv

def update_json_template():
    
    credentials_path = 'config/application_default_credentials.json'
    
    
    
    
    with open(credentials_path, 'r') as template_file:
        json_data = json.load(template_file)

    load_dotenv()
    json_data['type'] = os.environ['CLIENT_ID']
    json_data['project_id'] = os.environ['PROJECT_ID']
    json_data['private_key_id'] = os.environ['PRIVATE_KEY_ID']
    json_data['private_key'] = os.environ['PRIVATE_KEY']
    json_data['client_email'] = os.environ['CLIENT_EMAIL']
    json_data['client_id'] = os.environ['CLIENT_ID']
    json_data['auth_uri'] = os.environ['AUTH_URI']
    json_data['token_uri'] = os.environ['TOKEN_URI']
    json_data['auth_provider_x509_cert_url'] = os.environ['AUTH_PROVIDER']
    json_data['client_x509_cert_url'] = os.environ['CLIENT_X509']
    json_data['universe_domain'] = os.environ['UNIVERSE_DOMAIN']
    
    
    with open(credentials_path, 'w') as credentials_file:
        json.dump(json_data, credentials_file)
    
    
    # os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

