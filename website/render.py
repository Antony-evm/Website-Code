from jinja2 import Environment, FileSystemLoader

# Create a Jinja2 environment with the templates directory as the loader
env = Environment(loader=FileSystemLoader("templates"))


def render_template(input_file: str, output_file: str) -> None:
    """
    Render a template using Jinja2 and write the result to an output file.

    Args:
        input_file (str): The path to the input template file.
        output_file (str): The path to the output file
        where the rendered template will be written.
    """
    # Load the template from the input file
    template = env.get_template(input_file)

    # Render the template
    rendered = template.render()

    # Write the rendered template to the output file
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(rendered)


# Example usage
input_file = "topics_templates/projects_templates/used_cars/Used Cars.html"
output_file = "templates/topics_templates/projects_templates/used_cars/Used Cars.html"

render_template(input_file, output_file)
