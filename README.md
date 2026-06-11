# 🌐 Network Troubleshooting Toolkit

A Python-based command-line toolkit for IT network diagnostics.

## 🔧 Tools Included
- **Ping Test** — Check if a host is reachable
- **DNS Lookup** — Resolve hostname to IP address
- **IP Configuration** — View local network adapter info
- **Traceroute** — Trace the path packets take to a host
- **Run All + Save Report** — Runs all tools and saves output to a file

## 💻 Technologies
- Python 3
- Colorama (colored terminal output)
- Built-in modules: socket, subprocess, platform

## 🚀 How to Run

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/network-troubleshooting-toolkit.git

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the toolkit
python network_toolkit.py