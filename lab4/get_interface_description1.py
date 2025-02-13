from netmiko import ConnectHandler

# List of routers in the topology
routers = [
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
]

# List of "show" commands to execute
show_commands = [
    "show interface description",
    "show ip interface brief",
    "show version",
    "show running-config",
    "show arp",
    "show cdp neighbors",
]

# Loop through each router
for router in routers:
    try:
        print(f"\nConnecting to {router['ip']}...")

        # Establish the connection
        net_connect = ConnectHandler(**router)

        # Execute and display each command
        for command in show_commands:
            print(f"\nExecuting '{command}' on {router['ip']}:\n" + "-"*100)
            output = net_connect.send_command(command)
            print(output)
            print("-"*100)

        # Disconnect from the device
        net_connect.disconnect()
        print(f"\nDisconnected from {router['ip']}.")

    except Exception as e:
        print(f"An error occurred while connecting to {router['ip']}: {e}")
