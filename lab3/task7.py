from jinja2 import Environment, FileSystemLoader
import yaml

# Set up Jinja2 environment and load the template
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template-task6.j2")

# Load interface data from YAML file
with open("data-task7.yml") as f:
    interfaces = yaml.load(f, Loader=yaml.SafeLoader)

# Render the template with the interface list and print the result
print(template.render(interface_list=interfaces))
