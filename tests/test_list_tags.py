import unittest

from src.ydnatl.tags.lists import (
    UnorderedList,
    OrderedList,
    ListItem,
    Datalist,
    DescriptionDetails,
    DescriptionList,
    DescriptionTerm,
)


class TestListElements(unittest.TestCase):
    def test_unordered_list_tag(self):
        """Test that UnorderedList renders with the correct tag and content."""
        ul = UnorderedList("Simple Item")
        self.assertEqual(ul.tag, "ul")
        rendered = ul.render()
        self.assertTrue(rendered.startswith("<ul"))
        self.assertTrue(rendered.endswith("</ul>"))
        self.assertIn("Simple Item", rendered)

    def test_ordered_list_tag(self):
        """Test that OrderedList renders with the correct tag and content."""
        ol = OrderedList("Simple Item")
        self.assertEqual(ol.tag, "ol")
        rendered = ol.render()
        self.assertTrue(rendered.startswith("<ol"))
        self.assertTrue(rendered.endswith("</ol>"))
        self.assertIn("Simple Item", rendered)

    def test_list_item_tag(self):
        """Test that ListItem renders with the correct tag and content."""
        li = ListItem("List item content")
        self.assertEqual(li.tag, "li")
        rendered = li.render()
        self.assertTrue(rendered.startswith("<li"))
        self.assertTrue(rendered.endswith("</li>"))
        self.assertIn("List item content", rendered)

    def test_unordered_list_with_items(self):
        """Test the static with_items method on UnorderedList."""
        ul = UnorderedList.with_items("Item 1", ListItem("Item 2"), "Item 3")
        self.assertEqual(ul.tag, "ul")
        for child in ul.children:
            self.assertEqual(child.tag, "li")
        rendered = ul.render()
        self.assertIn("Item 1", rendered)
        self.assertIn("Item 2", rendered)
        self.assertIn("Item 3", rendered)

    def test_ordered_list_with_items(self):
        """Test the static with_items method on OrderedList."""
        ol = OrderedList.with_items("First", "Second", ListItem("Third"))
        self.assertEqual(ol.tag, "ol")
        for child in ol.children:
            self.assertEqual(child.tag, "li")
        rendered = ol.render()
        self.assertIn("First", rendered)
        self.assertIn("Second", rendered)
        self.assertIn("Third", rendered)

    def test_datalist_render(self):
        """Test that Datalist renders with the correct tag and content."""
        datalist = Datalist("Option1", "Option2")
        self.assertEqual(datalist.tag, "datalist")
        rendered = datalist.render()
        self.assertTrue(rendered.startswith("<datalist"))
        self.assertTrue(rendered.endswith("</datalist>"))
        self.assertIn("Option1", rendered)
        self.assertIn("Option2", rendered)

    def test_description_details_render(self):
        """Test that DescriptionDetails renders with the correct tag and content."""
        dd = DescriptionDetails("A detailed description")
        self.assertEqual(dd.tag, "dd")
        rendered = dd.render()
        self.assertTrue(rendered.startswith("<dd"))
        self.assertTrue(rendered.endswith("</dd>"))
        self.assertIn("A detailed description", rendered)

    def test_description_list_render(self):
        """Test that DescriptionList renders correctly and can contain dt and dd elements."""
        dl = DescriptionList()
        dt = DescriptionTerm("Term")
        dd = DescriptionDetails("Definition")
        dl.append(dt)
        dl.append(dd)
        self.assertEqual(dl.tag, "dl")
        rendered = dl.render()
        self.assertTrue(rendered.startswith("<dl"))
        self.assertTrue(rendered.endswith("</dl>"))
        self.assertIn("<dt>", rendered)
        self.assertIn("<dd>", rendered)
        self.assertIn("Term", rendered)
        self.assertIn("Definition", rendered)

    def test_description_term_render(self):
        """Test that DescriptionTerm renders with the correct tag and content."""
        dt = DescriptionTerm("Definition term")
        self.assertEqual(dt.tag, "dt")
        rendered = dt.render()
        self.assertTrue(rendered.startswith("<dt"))
        self.assertTrue(rendered.endswith("</dt>"))
        self.assertIn("Definition term", rendered)
