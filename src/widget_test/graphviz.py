import requests

from widget_test._jinja import get_template


class Graphviz:
    def _repr_html_(self) -> str:
        return get_template("d3-graphviz.jinja").render()
