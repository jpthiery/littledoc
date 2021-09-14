from jinja2 import Template


def write(module: dict) -> str:
    with open('smalldoc/onepage.md.jinja', 'r') as template_file:
        template = Template(template_file.read())
        return template.render(module=module)
