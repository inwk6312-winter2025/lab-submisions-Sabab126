from netmiko import Netmiko
import logging

# Enable logging to capture Netmiko debug output
logging.basicConfig(filename="netmiko_log.txt", level=logging.DEBUG)

# List of devices to connect to
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",  # Device IP address
        "username": "student",  # SSH username
        "password": "Meilab123",  # SSH password
        "port": 22,  # SSH port (default is 22)
    }
]

# Loop through each device to send the configuration
for device in devices:
    try:
        # Establish the connection to the device
        net_connect = Netmiko(**device)
        
        # Send the configuration from the 'changes.txt' file
        output = net_connect.send_config_from_file('changes.txt')
        
        # Print the output (confirmation of the configuration)
        print(output)

        # Disconnect from the device
        net_connect.disconnect()
        print(f"Disconnected from {device['ip']}.")

    except Exception as e:
        print(f"An error occurred with {device['ip']}: {e}")
