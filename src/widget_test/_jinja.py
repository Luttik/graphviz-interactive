from jinja2 import Environment, PackageLoader, Template


def get_template(file_name: str) -> Template:
    env = Environment(
        loader=PackageLoader("widget_test", "templates"),
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    return env.get_template(file_name)