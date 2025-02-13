import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import Netmiko

# Load the YAML files
hosts = yaml.load(open('hosts.yml'), Loader=yaml.SafeLoader)
interfaces = yaml.load(open('interfaces.yml'), Loader=yaml.SafeLoader)

# Set up Jinja2 environment for template rendering
env = Environment(loader=FileSystemLoader('.'), trim_blocks=True, autoescape=True)

# Load the Jinja2 template
template = env.get_template('interfaces_config_template.j2')

# Render the loopback interface configuration using the data from interfaces.yml
loopback_config = template.render(data=interfaces)

# Iterate over each host in the hosts YAML file
for host in hosts["hosts"]:
    try:
        # Establish SSH connection using Netmiko
        net_connect = Netmiko(
            host=host["name"],
            username=host["username"],
            password=host["password"],
            port=host["port"],
            device_type=host["type"]
        )
        print(f"Logged into {host['name']} successfully")

        # Push the configuration to the device
        output = net_connect.send_config_set(loopback_config.split("\n"))
        print(f"Pushed config into {host['name']} successfully")

        # Disconnect from the device
        net_connect.disconnect()

    except Exception as e:
        print(f"Failed to configure {host['name']}: {e}")

print("Done!")
