import socket
import threading

# Port Scanner
def scan_target(target, start_port, end_port):
    print(f"\n🔎 Scanning {target} from port {start_port} to {end_port}...\n")
    
    def scan_port(port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            if s.connect_ex((target, port)) == 0:
                print(f"✅ Port {port} is OPEN")
            s.close()
        except Exception as e:
            print(f"❌ Error scanning port {port}: {e}")

    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(port,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# Brute Force (Basic Dictionary Attack)
def brute_force_login(target, username, password_list):
    print(f"\n🔓 Attempting brute-force attack on {target}...\n")

    for password in password_list:
        print(f"Trying: {username} / {password}")
        # Simulating authentication attempt (Replace with actual login logic)
        if password == "admin123":  # Assume "admin123" is the correct password
            print(f"✅ SUCCESS: Username: {username} | Password: {password}")
            return True

    print("❌ Brute-force attack failed. No valid password found.")
    return False

# Main menu
def main():
    while True:
        print("\n🛠️ Penetration Testing Toolkit")
        print("1. Port Scanner")
        print("2. Brute Force Attack (Demo)")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            target = input("Enter target IP or domain: ")
            start_port = int(input("Enter start port: "))
            end_port = int(input("Enter end port: "))
            scan_target(target, start_port, end_port)

        elif choice == "2":
            target = input("Enter target login page URL (Demo): ")
            username = input("Enter username: ")
            password_list = ["password", "123456", "admin123", "welcome"]  # Example list
            brute_force_login(target, username, password_list)

        elif choice == "3":
            print("🔒 Exiting Toolkit. Stay Ethical!")
            break

        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
