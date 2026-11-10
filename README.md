# Python Port Scanner

A multithreaded TCP port scanner with banner grabbing, written in Python using only the standard library.

## Features
- Scans a range of TCP ports on a target host
- Uses 20 threads for faster scans
- Grabs service banners to identify software and versions
- Command-line options for target and port range

## Usage
```
python3 portscan.py <host> -s <start_port> -e <end_port>
```

Example:
```
python3 portscan.py 192.168.131.148 -s 1 -e 1024
```

## Example output
Scan of a Metasploitable2 VM in my home lab:
```
Port 21: open  220 (vsFTPd 2.3.4)
Port 22: open  SSH-2.0-OpenSSH_4.7p1 Debian-8ubuntu1
Port 25: open  220 metasploitable.localdomain ESMTP Postfix (Ubuntu)
```

## What I learned
- How TCP connection scanning works (`connect_ex`)
- Using threads to speed up network tasks
- How banners reveal software versions, e.g. vsFTPd 2.3.4 has a known backdoor (CVE-2011-2523)

## Lab setup
Kali Linux and Metasploitable2 running in VMware Workstation on an isolated network.

## Disclaimer
For educational use and authorized testing only. Only scan systems you own or have written permission to test.

## Future improvements
- Save results to a file
- Add service name detection
- Add UDP scanning
