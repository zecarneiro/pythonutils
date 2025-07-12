import sys
import os

# Fix import system_utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from enities import color

def debug_log(data: str):
    print(f"[DEBUG] {data}")

def warn_log(data: str):
    print(f"[{color.COLOR_YELLOW}WARN{color.COLOR_RESET}] {data}")

def error_log(data: str):
    print(f"[{color.COLOR_RED}ERROR{color.COLOR_RESET}] {data}")

def info_log(data: str):
    print(f"[{color.COLOR_BLUE}INFO{color.COLOR_RESET}] {data}")

def ok_log(data: str):
    print(f"[{color.COLOR_GREEN}INFO{color.COLOR_RESET}] {data}")

def prompt_log(data: str):
    print(f"{color.COLOR_GRAY}>>>{color.COLOR_RESET} {data}")

def title_log(data: str, length: int = -1, fill_char: str = "="):
    print(fill_char * length)
    print(data.center(length))
    print(fill_char * length)

def header_log(data: str, length: int = 50, fill_char: str = "-"):
    padding_length = length - len(data) - 2
    if padding_length <= 0:
        print(f" {data} ")
    else:
        left_length = padding_length // 2
        right_length = padding_length - left_length
        if left_length != right_length:
            right_length = left_length if left_length <= right_length else right_length
        print(f"{fill_char * left_length} {data} {fill_char * right_length}")

def separator_log(length: int = 6, fill_char: str = "-"):
    print(fill_char * length)
