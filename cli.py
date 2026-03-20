import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="WiFi Password Tool - Cross-platform & professional CLI",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "-l", "--list",
        action="store_true",
        help="List WiFi profiles"
    )
    parser.add_argument(
        "-s", "--show",
        type=str,
        metavar="NAME",
        help="Show password for one WiFi profile"
    )
    parser.add_argument(
        "-a", "--all",
        action="store_true",
        help="Show all WiFi passwords"
    )
    parser.add_argument(
        "-S", "--save",
        action="store_true",
        help="Save results to file"
    )

    # Examples نمایش داده میشن تو help
    parser.epilog = """Examples:
    python main.py -l
    python main.py --list
    python main.py -s "Wifi"
    python main.py --show "Wifi"
    python main.py -a -S
    python main.py --all --save
    """

    args = parser.parse_args()

    # Smart error: اگر user --show زده ولی اسم اشتباهه
    if args.show and not args.show.strip():
        parser.error("[!] Please provide a valid WiFi profile name for --show")

    return args