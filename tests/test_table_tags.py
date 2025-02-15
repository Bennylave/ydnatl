import unittest
import tempfile
import os
import csv
import json

from src.ydnatl.tags.table import (
    Table,
    TableFooter,
    TableHeaderCell,
    TableHeader,
    TableBody,
    TableDataCell,
    TableRow,
)


class TestTableElements(unittest.TestCase):

    def test_table_render(self):
        """Test that Table renders correctly with its children."""
        table = Table()
        row = TableRow()
        cell = TableDataCell("Cell 1")
        row.append(cell)
        table.append(row)

        rendered = table.render()
        self.assertTrue(rendered.startswith("<table"), msg=f"Rendered: {rendered}")
        self.assertTrue(rendered.endswith("</table>"), msg=f"Rendered: {rendered}")
        self.assertIn("Cell 1", rendered)

    def test_table_footer_render(self):
        """Test that TableFooter renders correctly."""
        footer = TableFooter("Footer Content")
        rendered = footer.render()
        self.assertTrue(rendered.startswith("<tfoot"), msg=f"Rendered: {rendered}")
        self.assertTrue(rendered.endswith("</tfoot>"), msg=f"Rendered: {rendered}")
        self.assertIn("Footer Content", rendered)

    def test_table_header_cell_render(self):
        """Test that TableHeaderCell renders correctly."""
        header_cell = TableHeaderCell("Header Cell")
        rendered = header_cell.render()
        self.assertTrue(rendered.startswith("<th"), msg=f"Rendered: {rendered}")
        self.assertTrue(rendered.endswith("</th>"), msg=f"Rendered: {rendered}")
        self.assertIn("Header Cell", rendered)

    def test_table_header_render(self):
        """Test that TableHeader renders correctly with its children."""
        header = TableHeader()
        header_cell = TableHeaderCell("Header1")
        header.append(header_cell)
        rendered = header.render()
        self.assertTrue(rendered.startswith("<thead"), msg=f"Rendered: {rendered}")
        self.assertTrue(rendered.endswith("</thead>"), msg=f"Rendered: {rendered}")
        self.assertIn("Header1", rendered)

    def test_table_body_render(self):
        """Test that TableBody renders correctly with its children."""
        body = TableBody()
        row = TableRow()
        cell = TableDataCell("Body Cell")
        row.append(cell)
        body.append(row)
        rendered = body.render()
        self.assertTrue(rendered.startswith("<tbody"), msg=f"Rendered: {rendered}")
        self.assertTrue(rendered.endswith("</tbody>"), msg=f"Rendered: {rendered}")
        self.assertIn("Body Cell", rendered)

    def test_table_from_csv(self):
        """Test that Table.from_csv correctly creates a table from a CSV file."""
        data = [
            ["Header1", "Header2"],
            ["Row1Cell1", "Row1Cell2"],
            ["Row2Cell1", "Row2Cell2"],
        ]
        with tempfile.NamedTemporaryFile(
            mode="w+", delete=False, newline="", encoding="utf-8"
        ) as tmp:
            writer = csv.writer(tmp)
            for row in data:
                writer.writerow(row)
            tmp_file_name = tmp.name

        try:
            table = Table.from_csv(tmp_file_name)
            self.assertEqual(len(table.children), len(data))
            for row_index, row in enumerate(table.children):
                self.assertEqual(row.__class__.__name__, "TableRow")
                self.assertEqual(len(row.children), len(data[row_index]))
                for cell_index, cell in enumerate(row.children):
                    self.assertEqual(cell.__class__.__name__, "TableDataCell")
                    self.assertIn(data[row_index][cell_index], cell.render())
        finally:
            os.remove(tmp_file_name)

    def test_table_from_json(self):
        """Test that Table.from_json correctly creates a table from a JSON file."""
        data = [
            ["Header1", "Header2"],
            ["Row1Cell1", "Row1Cell2"],
            ["Row2Cell1", "Row2Cell2"],
        ]
        with tempfile.NamedTemporaryFile(
            mode="w+", delete=False, encoding="utf-8"
        ) as tmp:
            json.dump(data, tmp)
            tmp_file_name = tmp.name
        try:
            table = Table.from_json(tmp_file_name)
            self.assertEqual(len(table.children), len(data))
            for row_index, row in enumerate(table.children):
                self.assertEqual(row.__class__.__name__, "TableRow")
                self.assertEqual(len(row.children), len(data[row_index]))
                for cell_index, cell in enumerate(row.children):
                    self.assertEqual(cell.__class__.__name__, "TableDataCell")
                    self.assertIn(data[row_index][cell_index], cell.render())
        finally:
            os.remove(tmp_file_name)
