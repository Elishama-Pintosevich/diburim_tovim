from google.cloud import storage



def upload_file(bucket_name, mp3_bytes, destination_blob_name):
    """Uploads a file to the bucket."""
    
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    
    generation_match_precondition = 0

    blob.upload_from_string(mp3_bytes, content_type='audio/mpeg')

    return True