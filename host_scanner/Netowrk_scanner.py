from scapy.all import ARP, Ether, srp
import socket

def scan_router(router_ip):
    print(f"Scanning devices connected to the router with IP: {router_ip}...\n")
    print("Keep patiine.")

    # Define the target IP range based on the router IP
    ip_range = f"{router_ip}/24"

    # Create an ARP request packet to broadcast
    arp_request = ARP(pdst=ip_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request

    # Send the packet and get the response
    answered_list = srp(arp_request_broadcast, timeout=2, verbose=False)[0]

    # List to store the details of connected devices
    devices = []

    for sent, received in answered_list:
        # Try to get the hostname of the device
        try:
            device_name = socket.gethostbyaddr(received.psrc)[0]
        except socket.herror:
            device_name = "Unknown"

        devices.append({"IP": received.psrc, "MAC": received.hwsrc, "Name": device_name})

    # Display the result
    print(f"Found {len(devices)} devices connected:\n")
    print("IP Address\t\tMAC Address\t\tDevice Name")
    print("-" * 60)
    for device in devices:
        print(f"{device['IP']}\t{device['MAC']}\t{device['Name']}")

    return devices

if __name__ == "__main__":
    # Prompt user for router IP
    router_ip = input("Enter your router's IP address (e.g., 192.168.1.1): ")

    try:
        connected_devices = scan_router(router_ip)
    except Exception as e:
        print(f"Error: {e}")
