import subprocess
import re

def get_profiles():
    try:
        output = subprocess.check_output(
            ["netsh", "wlan", "show", "profiles"],
            encoding="utf-8", errors="ignore"
        )
        profiles = re.findall(r"All User Profile\s*:\s*(.*)", output)
        profiles = [p.strip() for p in profiles if p.strip()]
        return list(dict.fromkeys(profiles))
    except subprocess.CalledProcessError:
        return []

def get_password(profile):
    try:
        output = subprocess.check_output(
            ["netsh", "wlan", "show", "profile", profile, "key=clear"],
            encoding="utf-8", errors="ignore"
        )
        match = re.search(r"Key Content\s*:\s*(.*)", output)
        return match.group(1) if match else None
    except subprocess.CalledProcessError:
        return None