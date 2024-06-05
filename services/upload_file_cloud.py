from google.cloud import storage
from google.oauth2 import service_account
import json
import os




def get_credentials_from_json_env():
    # Get the JSON string from the environment variable
    json_str = os.getenv('FILE')
    if not json_str:
        raise EnvironmentError("The GOOGLE_CLOUD_CREDENTIALS_JSON environment variable is not set or is empty")

    # Parse the JSON string
    service_account_info = json.loads(json_str)
    
    # Create credentials from the parsed JSON
    credentials = service_account.Credentials.from_service_account_info(service_account_info)
    return credentials


def upload_file(bucket_name, mp3_bytes, destination_blob_name):
    """Uploads a file to the bucket."""
    
    credentials = get_credentials_from_json_env()

    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    
    generation_match_precondition = 0

    blob.upload_from_string(mp3_bytes, content_type='audio/mpeg')

    return True