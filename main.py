from core.wifi import get_profiles, get_password
from cli import parse_args
from utils import print_result
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

OUTPUT_FILE = "wifi_passwords.txt"


def list_profiles(profiles):
    for p in profiles:
        print(f"• {p}")


def show_single(profile, profiles):
    if profile not in profiles:
        print("[!] WiFi not found")
        return None

    try:
        password = get_password(profile)
    except Exception as e:
        print(f"[!] Error fetching {profile}: {e}")
        return None

    print_result(profile, password)
    return {profile: password}


def fetch_all(profiles, max_workers=5):
    results = {}
    lock = Lock()

    def worker(profile):
        try:
            pw = get_password(profile)
        except Exception:
            pw = None

        with lock:
            results[profile] = pw
            print_result(profile, pw)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(worker, p) for p in profiles]

        for _ in as_completed(futures):
            pass  # فقط برای sync بهتر

    return results


def save_results(results):
    if not results:
        return

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for k, v in results.items():
            f.write(f"{k} -> {v}\n")

    print(f"\n[+] Saved to {OUTPUT_FILE}")


def main():
    args = parse_args()
    profiles = get_profiles()

    if not profiles:
        print("[!] No WiFi profiles found")
        return

    results = None

    if args.list:
        list_profiles(profiles)

    elif args.show:
        results = show_single(args.show, profiles)

    else:
        results = fetch_all(profiles)

    if args.save:
        save_results(results)


if __name__ == "__main__":
    main()