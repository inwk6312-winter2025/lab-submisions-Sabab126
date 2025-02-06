from jinja2 import Environment, FileSystemLoader

# Set up Jinja2 environment and load the template
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template-task6.j2")

# Define the list of interfaces with details
interfaces = [
    {
        "name": "GigabitEthernet0/1",
        "desc": "uplink port",
        "uplink": True
    },
    {
        "name": "GigabitEthernet0/2",
        "desc": "Server port number one",
        "vlan": 10
    },
    {
        "name": "GigabitEthernet0/3",
        "desc": "Server port number two",
        "vlan": 10
    }
]

# Render the template with the list of interfaces and print the result
print(template.render(interface_list=interfaces))
