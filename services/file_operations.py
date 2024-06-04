import os



def create_file(file, path):
    with open(path, "wb") as out:
        out.write(file)
        
def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)      


