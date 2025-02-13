from netmiko import Netmiko

# List of routers in the topology
routers = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",
        "username": "student",
        "password": "Meilab123",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",
        "username": "student",
        "password": "Meilab123",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",
        "username": "student",
        "password": "Meilab123",
        "port": "22",
    },
]

# Iterate through each router and fetch interface details
for router in routers:
    print(f"\nConnecting to {router['ip']}...\n")
    
    try:
        # Establish SSH connection
        net_connect = Netmiko(**router)
        
        # Run command and parse output
        output = net_connect.send_command("show ip interface brief", use_textfsm=True)
        
        # Disconnect the session
        net_connect.disconnect()
        
        # Print all interfaces for the router
        print(f"Interfaces on {router['ip']}:")
        print("-" * 50)

        if isinstance(output, list) and len(output) > 0:
            for interface in output:
                print(interface.get("interface", "Unknown Interface"))  # Ensure key exists
        else:
            print("No interface data found.")

        print("-" * 50)

    except Exception as e:
        print(f"Failed to retrieve data from {router['ip']}. Error: {e}")
