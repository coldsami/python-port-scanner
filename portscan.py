import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

def get_service(port):
    try:
        return socket.getservbyport(port, "tcp")
    except OSError:
        return "unknown"

def scan_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    if s.connect_ex((host, port)) != 0:
        s.close()
        return None
    try:
        banner = s.recv(1024).decode(errors="ignore").strip()
    except Exception:
        banner = ""
    s.close()
    return port, get_service(port), banner

parser = argparse.ArgumentParser(description="Simple port scanner")
parser.add_argument("host")
parser.add_argument("-s", "--start", type=int, default=1)
parser.add_argument("-e", "--end", type=int, default=1024)
args = parser.parse_args()

print(f"Scanning {args.host}...")
with ThreadPoolExecutor(max_workers=20) as pool:
    results = pool.map(lambda p: scan_port(args.host, p),
                       range(args.start, args.end + 1))
    for r in results:
        if r:
            print(f"Port {r[0]} ({r[1]}): open  {r[2]}")
