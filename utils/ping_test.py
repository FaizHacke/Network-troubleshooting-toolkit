import subprocess
import platform
from colorama import Fore, Style

def run_ping(host):
    print(f"\n{Fore.CYAN}[ PING TEST ] Target: {host}{Style.RESET_ALL}")
    print("-" * 45)

    # Windows uses -n, Linux/Mac uses -c
    param = "-n" if platform.system().lower() == "windows" else "-c"

    try:
        result = subprocess.run(
            ["ping", param, "4", host],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(f"{Fore.GREEN}✔ Host is reachable{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}✘ Host is unreachable{Style.RESET_ALL}")

        print(result.stdout)
        return result.stdout

    except Exception as e:
        error = f"Error running ping: {e}"
        print(f"{Fore.RED}{error}{Style.RESET_ALL}")
        return error
    