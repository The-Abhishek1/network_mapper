import socket
import ipaddress

#User Defined Modules
import device_details
import live_hosts
import network_map

# -------------------
# GET THE LOCAL IP
# ------------------

def get_local_ip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	try:
		s.connect(('8.8.8.8', 80))
		ip = s.getsockname()[0]
		return ip
	except Exception:
		return None
	finally:
		s.close()
		
# ----------------------
# GET NETWORK FROM USER
# ----------------------
def get_network_from_user():
	user_input = input("\nEnter network (e.g. 192.168.1.0/24) or press Enter for auto-detect: ").strip()

	if user_input:
		try:
			network = ipaddress.IPv4Network(user_input, strict=False)
		except ValueError:
			print("[!] Invalid network format")
			exit(1)
	else:
		local_ip = get_local_ip()

		if not local_ip:
			print("[!] Could not auo-detect local IPv4 address")
			sys.exit(1)

		try:
			network = ipaddress.IPv4Network(f"{local_ip}/24", strict=False)
		except ValueError:
			print(f"[!] Invalid local IP detected: {local_ip}")
			sys.exit(1)

	return (
		str(network.network_address),
		str(network.netmask),
		list(network.hosts())
	)

network_addr, netmask, hosts = get_network_from_user()
print(f"\nScanning network: {network_addr}/{netmask}\n")

# ---------------------------------
# SCAN LOCAL NETWORK FOR LIVE HOSTS
# ---------------------------------

live = live_hosts.ping_sweep_threaded(hosts, 1, 100)
print(f"\nNo. of Active hosts: {len(live)}")

# ----------------
# SCAN DETAILS 
# ----------------

devices = device_details.scan_details(live)

# -------------------------
# PRINTING DEVICE DETAILS
# ------------------------

device_details.print_table(devices)

# --------------
# NETWORK MAP
# --------------
gateway = get_local_ip()
g = ".".join(gateway[0].split(".")[:-1])+".1"
network_map.map(devices,g)


