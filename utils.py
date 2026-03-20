from colorama import Fore, Style, init
init(autoreset=True)

def print_result(profile, password):
    pw = password if password else "NO PASSWORD"
    print(f"{Fore.GREEN}[+] {Style.BRIGHT}{profile:<25}{Style.RESET_ALL} | {Fore.CYAN}{pw}")