from colorama import Fore, Style, init
from utils.ping_test import run_ping
from utils.dns_lookup import run_dns_lookup
from utils.ip_config import run_ip_config
from utils.traceroute import run_traceroute
from datetime import datetime
import os

init(autoreset=True)

def print_banner():
    print(f"""
{Fore.CYAN}
╔══════════════════════════════════════════════╗
║       NETWORK TROUBLESHOOTING TOOLKIT        ║
║            IT Support Utility v1.0           ║
╚══════════════════════════════════════════════╝
{Style.RESET_ALL}""")

def save_report(content, filename):
    os.makedirs("reports", exist_ok=True)
    filepath = f"reports/{filename}"
    with open(filepath, "w") as f:
        f.write(content)
    print(f"\n{Fore.GREEN}✔ Report saved to: {filepath}{Style.RESET_ALL}")

def main():
    print_banner()

    while True:
        print(f"\n{Fore.YELLOW}Select a tool:{Style.RESET_ALL}")
        print("  [1] Ping Test")
        print("  [2] DNS Lookup")
        print("  [3] IP Configuration Report")
        print("  [4] Traceroute")
        print("  [5] Run All Tools and Save Report")
        print("  [0] Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            host = input("Enter hostname or IP (e.g. google.com): ").strip()
            run_ping(host)

        elif choice == "2":
            host = input("Enter hostname (e.g. google.com): ").strip()
            run_dns_lookup(host)

        elif choice == "3":
            run_ip_config()

        elif choice == "4":
            host = input("Enter hostname or IP (e.g. google.com): ").strip()
            run_traceroute(host)

        elif choice == "5":
            host = input("Enter hostname or IP for ping/dns/traceroute (e.g. google.com): ").strip()
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"network_report_{timestamp}.txt"

            report = ""
            report += f"NETWORK REPORT — {timestamp}\n"
            report += "=" * 50 + "\n"
            report += run_ping(host)
            report += "\n" + run_dns_lookup(host)
            report += "\n" + run_ip_config()
            report += "\n" + run_traceroute(host)

            save_report(report, filename)

        elif choice == "0":
            print(f"\n{Fore.CYAN}Goodbye!{Style.RESET_ALL}\n")
            break

        else:
            print(f"{Fore.RED}Invalid choice. Please enter 1-5 or 0.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()