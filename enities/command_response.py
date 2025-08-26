import os
from dataclasses import dataclass

@dataclass
class CommandResponse:
    stdout: str = ""
    stderr: str = ""
    returncode: int = 0