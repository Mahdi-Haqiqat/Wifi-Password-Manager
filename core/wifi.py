import platform
from core import windows, linux, macos

def get_profiles():
    system = platform.system()
    if system == "Windows":
        return windows.get_profiles()
    elif system == "Linux":
        return linux.get_profiles()
    elif system == "Darwin":
        return macos.get_profiles()
    else:
        print(f"[!] Unsupported OS: {system}")
        return []

def get_password(profile):
    system = platform.system()
    if system == "Windows":
        return windows.get_password(profile)
    elif system == "Linux":
        return linux.get_password(profile)
    elif system == "Darwin":
        return macos.get_password(profile)
    else:
        return None