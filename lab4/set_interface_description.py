from netmiko import Netmiko

# List of devices
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",
        "username": "student",
        "password": "Meilab123",
        "port": "22",
    }
]

# Loopback interface configuration
loopback_config = [
    "interface Loopback1",
    "ip address 192.168.100.1 255.255.255.255",
    "description Loopback interface added via Netmiko",
    "no shutdown"
]

# Apply configuration to each device
for device in devices:
    print(f"\nConnecting to {device['ip']}...")

    # Establish SSH connection
    net_connect = Netmiko(**device)

    # Send configuration commands
    output = net_connect.send_config_set(loopback_config)
    print(output)

    # Save configuration
    save_output = net_connect.save_config()
    print("Configuration saved.")

    # Disconnect session
    net_connect.disconnect()
    print(f"Disconnected from {device['ip']}.")
