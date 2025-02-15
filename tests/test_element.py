import unittest

from src.ydnatl.core.element import HTMLElement


class TestElement(unittest.TestCase):

    def test_basic_render(self):
        """Test that a simple element with text renders correctly."""
        elem = HTMLElement("Hello", tag="div")
        expected = "<div>Hello</div>"
        self.assertEqual(elem.render(), expected)
        self.assertEqual(str(elem), expected)

    def test_attributes_rendering(self):
        """Test that attributes are rendered properly, including conversion of "class_name" to "class"."""
        elem = HTMLElement(
            tag="img",
            self_closing=True,
            src="image.jpg",
            alt="An image",
            class_name="my-class",
        )
        rendered = elem.render()
        self.assertIn("<img", rendered)
        self.assertIn('src="image.jpg"', rendered)
        self.assertIn('alt="An image"', rendered)
        self.assertIn('class="my-class"', rendered)
        self.assertTrue(rendered.endswith(" />"))

    def test_append_and_prepend(self):
        """Test appending and prepending children."""
        parent = HTMLElement(tag="div")
        child1 = HTMLElement("child1", tag="p")
        child2 = HTMLElement("child2", tag="span")
        parent.append(child1)
        parent.prepend(child2)
        rendered = parent.render()
        expected = f"<div>{child2.render()}{child1.render()}</div>"
        self.assertEqual(rendered, expected)

    def test_filter(self):
        """Test filtering children by condition."""
        parent = HTMLElement(tag="div")
        child1 = HTMLElement("child1", tag="p")
        child2 = HTMLElement("child2", tag="span")
        parent.append(child1, child2)
        result = list(parent.filter(lambda el: el.tag == "p"))
        self.assertEqual(result, [child1])

    def test_remove_all(self):
        """Test that remove_all correctly removes matching children."""
        parent = HTMLElement(tag="div")
        child1 = HTMLElement("child1", tag="p")
        child2 = HTMLElement("child2", tag="p")
        child3 = HTMLElement("child3", tag="span")
        parent.append(child1, child2, child3)
        parent.remove_all(lambda el: el.tag == "p")
        self.assertEqual(parent.count_children(), 1)
        self.assertEqual(parent.children[0].tag, "span")

    def test_pop_first_last(self):
        """Test first, last, and pop methods."""
        parent = HTMLElement(tag="div")
        child1 = HTMLElement("child1", tag="p")
        child2 = HTMLElement("child2", tag="span")
        parent.append(child1, child2)
        self.assertEqual(parent.first(), child1)
        self.assertEqual(parent.last(), child2)
        popped = parent.pop(0)
        self.assertEqual(popped, child1)
        self.assertEqual(parent.first(), child2)

    def test_attributes_methods(self):
        """Test add_attribute, get_attribute, has_attribute, and remove_attribute."""
        elem = HTMLElement(tag="div")
        elem.add_attribute("data-test", "value")
        self.assertEqual(elem.get_attribute("data-test"), "value")
        self.assertTrue(elem.has_attribute("data-test"))
        elem.remove_attribute("data-test")
        self.assertFalse(elem.has_attribute("data-test"))

    def test_generate_id(self):
        """Test that generate_id sets an id if not already present."""
        elem = HTMLElement(tag="div")
        self.assertIsNone(elem.get_attribute("id"))
        elem.generate_id()
        generated_id = elem.get_attribute("id")
        self.assertIsNotNone(generated_id)
        self.assertTrue(generated_id.startswith("el-"))
        self.assertEqual(len(generated_id), 9)

    def test_clone(self):
        """Test that clone creates a deep copy of the element."""
        elem = HTMLElement("Original", tag="div")
        elem.add_attribute("data-test", "value")
        clone = elem.clone()
        self.assertEqual(clone.render(), elem.render())
        clone.add_attribute("data-new", "new")
        self.assertNotEqual(clone.get_attributes(), elem.get_attributes())

    def test_find_by_attribute(self):
        """Test finding a child by attribute."""
        parent = HTMLElement(tag="div")
        child = HTMLElement("child", tag="p", id="unique")
        parent.append(child)
        found = parent.find_by_attribute("id", "unique")
        self.assertEqual(found, child)
        nested_parent = HTMLElement(tag="section")
        nested_child = HTMLElement("nested", tag="span", class_name="special")
        child.append(nested_parent)
        nested_parent.append(nested_child)
        found_nested = child.find_by_attribute("class_name", "special")
        self.assertEqual(found_nested, nested_child)

    def test_get_attributes(self):
        """Test retrieving attributes by specific keys and all attributes."""
        elem = HTMLElement(tag="div", a="1", b="2", c="3")
        attrs = elem.get_attributes("a", "c")
        self.assertEqual(attrs, {"a": "1", "c": "3"})
        all_attrs = elem.get_attributes()
        self.assertEqual(all_attrs, {"a": "1", "b": "2", "c": "3"})

    def test_count_children(self):
        """Test counting children."""
        parent = HTMLElement(tag="div")
        self.assertEqual(parent.count_children(), 0)
        child = HTMLElement("child", tag="p")
        parent.append(child)
        self.assertEqual(parent.count_children(), 1)

    def test_self_closing(self):
        """Test rendering of a self-closing element."""
        elem = HTMLElement(tag="br", self_closing=True)
        rendered = elem.render()
        self.assertEqual(rendered, "<br />")

    def test_text_property(self):
        """Test that the text property is set and rendered correctly."""
        elem = HTMLElement("Hello", tag="div")
        self.assertEqual(elem.text, "Hello")
        elem.text = "New Text"
        self.assertEqual(elem.text, "New Text")
        rendered = elem.render()
        self.assertIn("New Text", rendered)
