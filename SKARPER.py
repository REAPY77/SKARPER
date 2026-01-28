from ping3 import ping
import socket


target = ""

def get_subnet_prefix():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return '.'.join(local_ip.split('.')[:3]) + '.'


def scan_network(subnet_prefix, timeout=1):
    print("Scanning local network...")
    alive_ips = []

    for ip_suffix in range(256):
        ip = f"{subnet_prefix}{ip_suffix}"
        try:
            response_time = ping(ip, timeout=timeout)
            if response_time is not None:
                print(f"{ip} -> alive ({response_time:.3f}s)")
                alive_ips.append(ip)
            else:
                print(f"{ip} -> not detected")
        except Exception as e:
            print(f"{ip} -> error: {e}")

    print(f"\nFound {len(alive_ips)} active hosts.")
    return alive_ips

def single_target(target):
        target_ip = f"{target}"
        target_status = ping(target_ip)
        if target_status:
            print("target" + f"({target_ip})"+ " is online")
        else:
            print("target was not detected")


def main():
    print("------------Welcome to SKARPER -----------")

    subnet = get_subnet_prefix()
    local_ip = socket.gethostbyname(socket.gethostname())

    print(f"Local IP:    {local_ip}")
    print(f"Subnet:      {subnet}0-255")
    print(f"Scannable:   {subnet}0-255")

    print("\nOptions:")
    print("1) Single target scan")
    print("2) Entire local network scan")

    choice = input("\nEnter choice (1 or 2): ").strip()

    if choice == "2":
        scan_network(subnet)
    else:
        target = input("\nEnter target to scan: ").strip()
        single_target(target)


if __name__ == "__main__":
    main()
