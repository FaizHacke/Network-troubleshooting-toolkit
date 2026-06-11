import subprocess
import platform
from colorama import Fore, Style

def run_ip_config():
    print(f"\n{Fore.CYAN}[ IP CONFIGURATION REPORT ]{Style.RESET_ALL}")
    print("-" * 45)

    try:
        # Windows uses ipconfig, Linux/Mac uses ifconfig
        command = "ipconfig" if platform.system().lower() == "windows" else "ifconfig"
        result = subprocess.run(
            [command],
            capture_output=True,
            text=True
        )
        print(result.stdout)
        return result.stdout

    except Exception as e:
        error = f"Error getting IP config: {e}"
        print(f"{Fore.RED}{error}{Style.RESET_ALL}")
        return error