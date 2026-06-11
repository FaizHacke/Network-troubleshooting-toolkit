import subprocess
import platform
from colorama import Fore, Style

def run_traceroute(host):
    print(f"\n{Fore.CYAN}[ TRACEROUTE ] Target: {host}{Style.RESET_ALL}")
    print("-" * 45)

    try:
        # Windows uses tracert, Linux/Mac uses traceroute
        command = "tracert" if platform.system().lower() == "windows" else "traceroute"
        result = subprocess.run(
            [command, host],
            capture_output=True,
            text=True
        )
        print(result.stdout)
        return result.stdout

    except Exception as e:
        error = f"Error running traceroute: {e}"
        print(f"{Fore.RED}{error}{Style.RESET_ALL}")
        return error