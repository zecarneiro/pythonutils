import os
from dataclasses import dataclass, field
from typing import Union, List
from pathlib import Path


@dataclass
class CommandInfo:
    command: Union[str, Path]
    args: List[str] = None
    use_shell: bool = True
    verbose: bool = False
    env: dict[str, str] = field(default_factory=lambda: os.environ.copy())
    cwd: str = None
