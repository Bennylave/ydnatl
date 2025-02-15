from src.ydnatl.core.element import HTMLElement
import csv
import json

class Table(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "table"})

    @staticmethod
    def from_csv(file_path):
        table = Table()
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                table_row = TableRow()
                for cell in row:
                    table_row.append(TableDataCell(cell))
                table.append(table_row)
        return table

    @staticmethod
    def from_json(file_path):
        table = Table()
        with open(file_path, mode='r', encoding='utf-8') as file:
            data = json.load(file)
            for row in data:
                table_row = TableRow()
                for cell in row:
                    table_row.append(TableDataCell(cell))
                table.append(table_row)
        return table


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
