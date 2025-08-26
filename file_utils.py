import os
import json
import shutil
import sys
from typing import Type, List, TypeVar


# Fix import system_utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

T = TypeVar('T')

def resolve_path(arg: str) -> str:
    return os.path.normpath(arg)

def join_path(*args: str) -> str:
    full_path = ''
    for arg in args:
        full_path = os.path.join(full_path, arg)
    return full_path

def read_json_file(json_file: str, cls: Type[T]) -> T:
    with open(json_file, 'r') as f:
        data = json.load(f)
    return cls(**data)

def file_exist(file: str) -> bool:
    return is_file(file) or is_dir(file)

def is_file(file: str) -> bool:
    if len(file) <= 0:
        return False
    file = resolve_path(file)
    return os.path.isfile(file)

def is_dir(directory: str) -> bool:
    if len(directory) <= 0:
        return False
    directory = resolve_path(directory)
    return os.path.isdir(directory)

def delete_file(file: str):
    file = resolve_path(file)
    if is_file(file):
        os.remove(file)
    elif is_dir(file):
        shutil.rmtree(file)  # Deletes directory and all contents recursively

def is_valid_extension(filename: str, extensions: List[str]) -> bool:
    _, ext = os.path.splitext(filename)
    return ext.lower() in extensions
