import os
import json
import sys

# Fix import system_utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from enities.custom_encoder import CustomEncoder

def str_is_empty(data: str) -> bool:
    if not data or not data.strip():
        return True
    return False

def get_script_dir(file: str = None) -> str:
    if str_is_empty(file):
        file = __file__
    return os.path.dirname(os.path.abspath(file))

def object_to_string(data) -> str:
    return json.dumps(data, cls=CustomEncoder, indent=2)

def run_function(func, **args):
    if func:
        if args:
            func(args)
        else:
            func()