from scapy.all import *
import socket
from tabulate import tabulate

# --------------------
# MAC DETAILS
# --------------------

def get_mac(ip):
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast = broadcast / arp_request
    answered = srp(arp_broadcast, timeout=1, verbose=0)[0]
    if answered:
        return answered[0][1].hwsrc
    return None

# --------------------------------
# GETTING HOSTNAME USING NETBIOS
# --------------------------------
def get_hostname_netbios(ip):
	try:
		output = subprocess.check_output(
			["nmblookup", "-A", ip],
			stderr=subprocess.DEVNULL,
			timeout=2
		)
		for line in output.decode().splitlines():
			if "<00>" in line and "GROUP" not in line:
				return line.split()[0]
	except Exception:
		pass
	return ""

# -----------------------------
# GETTING HOSTNAME USING mDNS 
# -----------------------------

def get_hostname_mdns(ip):
	try:
		output =subprocess.check_output(
			["avahi-resolve-address", ip],
			stderr=subprocess.DEVNULL,
			timeout=2
		)
		return output.decode().split()[1]
	except Exception:
		pass

	return ""

# -----------------
# RESOLVE HOSTNAME
# -----------------
def resolve_hostname(ip):
	hostname = ""

	# Reverse DNS
	try:
		hostname = socket.gethostbyaddr(ip)[0]
		if hostname:
			return hostname
	except Exception:
		pass

	# NetBIOS
	hostname = get_hostname_netbios(ip)
	if hostname:
		return hostname

	# mDNS
	hostname = get_hostname_mdns(ip)
	if hostname:
		return hostname

	return ""

# ----------------
# SCAN DETAILS
# ----------------
def scan_details(live):
    devices = []
    for ip in live:
        mac = get_mac(ip)
        hostname = resolve_hostname(ip)
        devices.append({"ip":ip, "mac":mac, "hostname": hostname})
    return devices

# -------------------------
# PRINTING DEVICE DETAILS
# ------------------------
def print_table(devices):
    table = []
    for d in devices:
        table.append([
            d.get("ip","N/A"),
            d.get("mac","N/A"),
            d.get("hostname", "N/A")
        ])
	
    print("\n",tabulate(
        table,
        headers = ["IP Address", "MAC Address", "Hostname"],
        tablefmt = "grid"
    ),"\n")
