from jinja2 import Environment, FileSystemLoader

# Set up the Jinja2 environment and load the new template for this task
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template-task3.j2")

# Define the NetworkInterface class with an __init__ method
class NetworkInterface(object):
    def __init__(self, name, description, vlan, uplink=False):
        self.name = name
        self.description = description
        self.vlan = vlan
        self.uplink = uplink

# Create 10 instances of the NetworkInterface class for interfaces G0/1 to G0/10
interfaces = []
for i in range(1, 11):  # From G0/1 to G0/10
    interface = NetworkInterface(f"G0/{i}", f"Interface {i}", vlan=i)
    interfaces.append(interface)

# Render the template with the list of network interfaces
print(template.render(interfaces=interfaces))

