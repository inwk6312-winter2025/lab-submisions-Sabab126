from netmiko import Netmiko

# Define the router details
device = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.101",
    "username": "student",
    "password": "Meilab123",
    "port": "22",
}

# Establish the connection
net_connect = Netmiko(**device)

# Execute "show ip interface brief" with TextFSM parsing enabled
output = net_connect.send_command("show ip interface brief", use_textfsm=True)

# Disconnect from the device
net_connect.disconnect()

# Print the raw output to inspect its structure
print(f"Raw Output: {output}\n")

# Check if output is valid
if isinstance(output, list) and len(output) > 0:
    print("Available Keys in Output: ", output[0].keys())  # Display available keys
    print("\nInterface List:")
    print("-" * 50)
    
    # Iterate over interfaces and print using the correct key
    for interface in output:
        # Adjust this key based on printed output keys
        print(interface.get("interface", "Unknown Interface"))  
        
    print("-" * 50)
else:
    print("Failed to parse output using TextFSM or no data returned.")
