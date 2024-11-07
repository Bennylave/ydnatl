from src.ydnatl.core.element import HTMLElement


class Table(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "table"})

    @staticmethod
    def from_csv(file_path):
        pass

    @staticmethod
    def from_json(file_path):
        pass


class TableFooter(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "tfoot"})


class TableHeaderCell(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "th"})


class TableHeader(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "thead"})


class TableBody(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "tbody"})


class TableDataCell(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "td"})


class TableRow(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "tr"})
