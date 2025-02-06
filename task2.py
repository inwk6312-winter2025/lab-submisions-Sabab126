from jinja2 import Environment, FileSystemLoader

# Set up the Jinja2 environment and load the template
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template-task2.j2")

# Define the NetworkInterface class with an __init__ method
class NetworkInterface(object):
    def __init__(self, name, description, vlan, uplink=False):
        self.name = name
        self.description = description
        self.vlan = vlan
        self.uplink = uplink

# Create an instance of the NetworkInterface class
interface_obj = NetworkInterface("GigabitEthernet0/1", "Server Port", 10)

# Render the template with the network interface object
print(template.render(interface=interface_obj))
