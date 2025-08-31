from scapy.all import IP, ICMP, send

def send_one_packet(target_ip):
    packet = IP(dst=target_ip)/ICMP()
    send(packet, count=1)
    print(f"✅ Sent 1 packet to {target_ip}")

def main():
    while True:
        print("\n=== Packet Sender Menu ===")
        print("1. Send 1 packet")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            target_ip = input("Enter target IP address: ")
            send_one_packet(target_ip)
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
