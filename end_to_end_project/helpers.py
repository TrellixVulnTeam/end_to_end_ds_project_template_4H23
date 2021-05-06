import os
import config


def create_directory(path=config.base_dir, directory='directory'):
    directory_path = os.path.join(config.base_dir, directory)
    try:
        os.makedirs(directory_path, exist_ok=True)
        print(
            f"Directory '{directory}' created successfully, or already exists")
    except OSError as error:
        print(f"Directory '{directory}' can not be created, Error: {error}")


create_directory(directory='data/intermediate')
