import unittest

from core.tag import HTMLTag


class TestMainTag(unittest.TestCase):
    def test_tag_initialization(self):
        tag = HTMLTag("Hello", tag="p")
        self.assertEqual(tag.tag, "p")
        self.assertEqual(tag.text, "Hello")
        self.assertEqual(tag.children, [])
        self.assertEqual(tag.attributes, {})

    def test_tag_render(self):
        tag = HTMLTag("Hello", tag="p")
        self.assertEqual(tag.render(), "<p>Hello</p>")

    def test_tag_with_children(self):
        child1 = HTMLTag("Child 1", tag="span")
        child2 = HTMLTag("Child 2", tag="span")
        parent = HTMLTag([child1, child2], tag="div")
        self.assertEqual(parent.render(), "<div><span>Child 1</span><span>Child 2</span></div>")


# class TestSubclasses(unittest.TestCase):
#     def test_section(self):
#         section = Section(Div(H1("Hello World!"), Paragraph("This is a paragraph")))
#         self.assertIn("<section>", section.render())
#         self.assertIn("</section>", section.render())
#
#     def test_div(self):
#         div = Div(H1("Hello World!"), Paragraph("This is a paragraph"))
#         self.assertIn("<div>", div.render())
#         self.assertIn("</div>", div.render())
#
#     def test_button(self):
#         button = Button("Click me!")
#         self.assertEqual(button.render(), "<button>Click me!</button>")


if __name__ == "__main__":
    unittest.main()
