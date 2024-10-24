from core.tag import HTMLTag


class Table(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "table"})

    @staticmethod
    def from_csv(file_path):
        pass

    @staticmethod
    def from_json(file_path):
        pass


class TableFooter(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "tfoot"})


class TableHeaderCell(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "th"})


class TableHeader(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "thead"})


class TableBody(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "tbody"})


class TableDataCell(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "td"})


class TableRow(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "tr"})
