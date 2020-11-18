class ReprObject:

    def __init__(self, label: str) -> None:
        super().__init__()
        self.label = label

    def _repr_html_(self) -> str:
        return (
            "<script>function x() {document.getElementById('x').innerHTML = 'bla2'}</script>"
            "<button onclick=\"x()\">"
            f"{self.label}"
            "</button><div id=\"x\">bla</div>"
        )
