import socket
from colorama import Fore, Style

def run_dns_lookup(host):
    print(f"\n{Fore.CYAN}[ DNS LOOKUP ] Target: {host}{Style.RESET_ALL}")
    print("-" * 45)

    try:
        ip_address = socket.gethostbyname(host)
        result = f"Hostname : {host}\nIP Address: {ip_address}"
        print(f"{Fore.GREEN}✔ DNS resolved successfully{Style.RESET_ALL}")
        print(result)
        return result

    except socket.gaierror as e:
        error = f"✘ DNS lookup failed for {host}: {e}"
        print(f"{Fore.RED}{error}{Style.RESET_ALL}")
        return error