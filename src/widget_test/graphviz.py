import requests

from widget_test._jinja import get_template


class Graphviz:
    def _repr_html_(self) -> str:
        d3 = requests.get("https://d3js.org/d3.v5.min.js").text
        wasm = requests.get(
            "https://unpkg.com/@hpcc-js/wasm@0.3.11/dist/index.min.js"
        ).text
        d3_graphviz = requests.get(
            "https://unpkg.com/d3-graphviz@3.0.5/build/d3-graphviz.js"
        ).text
        return get_template("d3-graphviz.jinja").render(
            d3=d3, wasm=wasm, d3_graphviz=d3_graphviz
        )
