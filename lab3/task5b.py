from jinja2 import Environment, FileSystemLoader

# Set up the Jinja2 environment and load the template
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template-task5b.j2")

# Dictionary of interfaces and their descriptions
inter_dict = {
    "GigabitEthernet0/1": "Server port number one",
    "GigabitEthernet0/2": "Server port number two",
    "GigabitEthernet0/3": "Server port number three"
}

# Render the template with the dictionary and print the result
print(template.render(interface_dict=inter_dict))

