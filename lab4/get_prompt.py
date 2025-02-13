from netmiko import Netmiko, NetmikoTimeoutException, NetmikoAuthenticationException

# List of devices (3 routers)
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",  # Router 1
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",  # Enable secret password
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",  # Router 2
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",  # Enable secret password
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",  # Router 3
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",  # Enable secret password
        "port": "22",
    },
]

# Loop through each device
for device in devices:
    try:
        print(f"\nConnecting to {device['ip']}...")

        # Establish the connection
        net_connect = Netmiko(**device)

        # Print the default prompt (should be in enable mode)
        prompt = net_connect.find_prompt()
        print(f"Default prompt: {prompt}")

        # Issue the disable command and print the prompt
        net_connect.send_command_timing("disable")
        prompt = net_connect.find_prompt()
        print(f"After disable command: {prompt}")

        # Issue the enable command and print the prompt
        net_connect.enable()
        prompt = net_connect.find_prompt()
        print(f"After enable command: {prompt}")

        # Write the final prompt to a file
        with open(f"device_prompt_{device['ip']}.txt", "w") as file:
            file.write(prompt)

        # Close the connection
        net_connect.disconnect()
        print(f"Disconnected from {device['ip']}.")

    except NetmikoTimeoutException:
        print(f"Connection to {device['ip']} timed out. Please check the IP address or network connectivity.")
    except NetmikoAuthenticationException:
        print(f"Authentication failed for {device['ip']}. Please check the username, password, or enable secret.")
    except Exception as e:
        print(f"An error occurred with {device['ip']}: {e}")
