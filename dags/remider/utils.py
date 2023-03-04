import os
import pickle
import tempfile
from typing import Optional

def write_data(obj: object, dag_id: str, name: str) -> str:
    prefix = f"airlfow_{dag_id}_"
    temp_dir = tempfile.gettempdir()

    # check if temp directory is existed, and temp file will be overwritten
    existed = False
    for entry in os.listdir(temp_dir):
        temp_data_dir = os.path.join(temp_dir, entry)
        if os.path.isdir(temp_data_dir) and entry.startswith(prefix):
            existed = True
            break

    if not existed:
        temp_data_dir = tempfile.mkdtemp(prefix=prefix)

    obj_filepath = os.path.join(temp_data_dir, f"{name}.pkl")
    with open(obj_filepath, "wb") as f:
        pickle.dump(obj, f)

    return obj_filepath


def read_data(filepath: str) -> object:
    if not filepath:
        raise ValueError("please provide a vaild filepath")

    with open(filepath, "rb") as f:
        obj = pickle.load(f)

    return obj


def remove_data(filepath: Optional[str]) -> bool:
    try:
        os.remove(filepath)
        return True
    except (FileNotFoundError, TypeError):
        return False
