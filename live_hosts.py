from scapy.all import *
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging
import time

# ---------------------------------
# SCAN LOCAL NETWORK FOR LIVE HOSTS
# ---------------------------------

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
conf.verb = 0
conf.retry = 0

def ping_host(ip, timeout=1):
    pkt = IP(dst=str(ip)) / ICMP()
    reply = sr1(pkt, timeout=timeout, verbose=False)
    if reply:
        return str(ip)
    return None

def ping_sweep_threaded(hosts, timeout=1, threads=50):
    active_hosts = []

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = { executor.submit(ping_host, ip, timeout): ip
            for ip in hosts
         }

    for future in as_completed(futures):
        result = future.result()
        if result:
            print(f"[+] Host {result} is UP")
            active_hosts.append(result)

    return active_hosts

