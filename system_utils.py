import platform
from enities.platform_enum import EPlatform

def get_platform() -> EPlatform:
    if platform.system() == "Windows":
        return EPlatform.WINDOWS
    elif platform.system() == "Linux":
        return EPlatform.LINUX
    elif platform.system() == "Darwin":
        return EPlatform.MACOS
    else:
        return EPlatform.UNKNOWN

def is_windows() -> bool:
    return get_platform() == EPlatform.WINDOWS

def is_linux() -> bool:
    return get_platform() == EPlatform.LINUX

def is_macos() -> bool:
    return get_platform() == EPlatform.MACOS
