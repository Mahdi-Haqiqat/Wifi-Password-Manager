import subprocess

def get_profiles():
    try:
        output = subprocess.check_output(
            ["nmcli", "-t", "-f", "NAME", "connection", "show"],
            encoding="utf-8"
        )
        profiles = [p.strip() for p in output.splitlines() if p.strip()]
        return list(dict.fromkeys(profiles))
    except FileNotFoundError:
        print("[!] nmcli not found. Skipping Linux WiFi scan.")
        return []

def get_password(profile):
    try:
        output = subprocess.check_output(
            ["nmcli", "-s", "-g", "802-11-wireless-security.psk", "connection", "show", profile],
            encoding="utf-8"
        )
        return output.strip() or None
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None