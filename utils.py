import zipfile


def extract(path_zip: str, dir_extract: str):
    with zipfile.ZipFile(path_zip, 'r') as zip_ref:
        zip_ref.extractall(dir_extract)


def mkdir(dir_name: str):
    
