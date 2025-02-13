from netmiko import Netmiko, NetmikoTimeoutException, NetmikoAuthenticationException

# List of devices (all routers in the topology)
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",  # Router 1
        "username": "student",
        "password": "Meilab123",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",  # Router 2
        "username": "student",
        "password": "Meilab123",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",  # Router 3
        "username": "student",
        "password": "Meilab123",
        "port": "22",
    },
    # Add more routers as needed
]

# Loop through each device
for device in devices:
    try:
        print(f"\nConnecting to {device['ip']}...")

        # Establish the connection
        net_connect = Netmiko(**device)

        # Send the "show running-config" command and capture the output
        output = net_connect.send_command("show running-config")

        # Print the running configuration
        print(f"\nRunning Configuration for {device['ip']}:\n")
        print(output)

        # Disconnect from the device
        net_connect.disconnect()
        print(f"\nDisconnected from {device['ip']}.")

    except NetmikoTimeoutException:
        print(f"Connection to {device['ip']} timed out. Please check the IP address or network connectivity.")
    except NetmikoAuthenticationException:
        print(f"Authentication failed for {device['ip']}. Please check the username, password, or enable secret.")
    except Exception as e:
        print(f"An error occurred with {device['ip']}: {e}")
