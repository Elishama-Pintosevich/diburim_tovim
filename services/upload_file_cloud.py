from google.cloud import storage



def upload_file(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    
    generation_match_precondition = 0

    blob.upload_from_filename(source_file_name, if_generation_match=generation_match_precondition)

    return True