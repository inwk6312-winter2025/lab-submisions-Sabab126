from netmiko import Netmiko

# List of devices (2 routers)
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
]

# Loop through each device
for device in devices:
    # Establish the connection
    net_connect = Netmiko(**device)

    # Send the "show version" command and capture the output
    output = net_connect.send_command("show version")

    # Disconnect from the device
    net_connect.disconnect()

    # Find the uptime information in the output
    result = output.find("uptime is")  # Find the starting index of "uptime is"
    begin = int(result)  # Convert the result to an integer
    end = begin + 38  # Calculate the end index (38 characters after "uptime is")

    # Extract and print the uptime information
    uptime_info = output[begin:end]  # Slice the output to get the uptime information
    print(f"{device['ip']} => {uptime_info}")
