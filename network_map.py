import networkx as nx
import matplotlib.pyplot as plt
import math


# -------------
# DEVICE TYPE
# -------------
def get_device_type(hostname: str, ip:str, gateway:str) -> str:

	h = hostname.lower()
	if "router" in h or "gateway" in h or ip == gateway:
		return "Router"
	if "android" in h or "iphone" in h:
		return "Mobile"
	if "printer" in h:
		return "Printer"
	if not hostname:
		return "Unknown"
	return "Host" 
	
# ----------------------
# NETWORK MAP
# ----------------------
def map(devices, gateway):
	G = nx.Graph()
	G.add_node(gateway, label=f"{gateway}\nGateway")

	for device in devices:
		ip = device.get("ip", "N/A")
		mac = device.get("mac", "N/A")
		hostname = device.get("hostname", "N/A")

		device_type = get_device_type(hostname,ip, gateway)
		label = (
			f"{ip}\n"
			f"{mac}\n"
			f"{hostname}\n"
			f"{device_type}"
		)

		G.add_node(ip, label=label)
		G.add_edge(gateway, ip)

	pos = {}
	pos[gateway] = (0,0)

	count = len(devices)
	radius = 4

	for i, device in enumerate(devices):
		angle = 2 * math.pi * i / max(count,1)
		x = radius * math.cos(angle)
		y = radius * math.sin(angle)
		pos[device["ip"]] = (x,y)

	labels = nx.get_node_attributes(G, "label")

	node_colors = []
	node_sizes = []

	for node in G.nodes():
		if node == gateway:
			node_colors.append("orange")
			node_sizes.append(3500)
		else:
			node_colors.append("lightblue")
			node_sizes.append(2400)

	plt.figure(figsize=(14, 14))

	nx.draw(G, pos, labels= labels, with_labels=True, node_color=node_colors, node_size=node_sizes, font_size=8, edge_color="gray")

	plt.title("Logical Network Map (Gateway-Centrix View)", fontsize=14)
	plt.show()
