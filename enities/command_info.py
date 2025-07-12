import os
from dataclasses import dataclass

@dataclass
class CommandInfo:
    command: str
    use_shell: bool = True
    verbose: bool = False
    env = os.environ.copy()
    cwd: str = None