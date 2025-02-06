from jinja2 import Environment, FileSystemLoader

# Set up the Jinja2 environment and load the template
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template-task5a.j2")

# List of interfaces to be processed by the template
inter_list = [
    "GigabitEthernet0/1",
    "GigabitEthernet0/2",
    "GigabitEthernet0/3"
]

# Render the template with the interface list and print the result
print(template.render(interface_list=inter_list))
