import subprocess

def get_profiles():
    try:
        output = subprocess.check_output(
            ["/usr/sbin/networksetup", "-listpreferredwirelessnetworks", "en0"],
            encoding="utf-8"
        )
        profiles = [line.strip() for line in output.splitlines() if line.strip() and "Preferred Networks on" not in line]
        return list(dict.fromkeys(profiles))
    except subprocess.CalledProcessError:
        return []

def get_password(profile):
    try:
        output = subprocess.check_output(
            ["security", "find-generic-password", "-D", "AirPort network password", "-a", profile, "-w"],
            encoding="utf-8", errors="ignore"
        )
        return output.strip()
    except subprocess.CalledProcessError:
        return None