from widget_test._jinja import get_template
import requests


class Graphviz:
    def _repr_html_(self) -> str:
        d3 = requests.get('https://d3js.org/d3.v5.min.js').text
        return get_template('d3-graphviz.jinja').render(d3=d3)
