import unittest

from src.ydnatl.tags.layout import (
    Div,
    Section,
    Header,
    Nav,
    Footer,
    HorizontalRule,
    Main,
)


class TestLayoutTags(unittest.TestCase):

    def test_div_render(self):
        """Test that Div renders correctly with the proper tag."""
        div = Div("This is a div")
        self.assertEqual(div.tag, "div")
        rendered = div.render()
        self.assertTrue(rendered.startswith("<div"))
        self.assertTrue(rendered.endswith("</div>"))
        self.assertIn("This is a div", rendered)

    def test_section_render(self):
        """Test that Section renders correctly with the proper tag."""
        section = Section("Section Content")
        self.assertEqual(section.tag, "section")
        rendered = section.render()
        self.assertTrue(rendered.startswith("<section"))
        self.assertTrue(rendered.endswith("</section>"))
        self.assertIn("Section Content", rendered)

    def test_header_render(self):
        """Test that Header renders correctly with the proper tag."""
        header = Header("Header Content")
        self.assertEqual(header.tag, "header")
        rendered = header.render()
        self.assertTrue(rendered.startswith("<header"))
        self.assertTrue(rendered.endswith("</header>"))
        self.assertIn("Header Content", rendered)

    def test_nav_render(self):
        """Test that Nav renders correctly with the proper tag."""
        nav = Nav("Navigation Content")
        self.assertEqual(nav.tag, "nav")
        rendered = nav.render()
        self.assertTrue(rendered.startswith("<nav"))
        self.assertTrue(rendered.endswith("</nav>"))
        self.assertIn("Navigation Content", rendered)

    def test_footer_render(self):
        """Test that Footer renders correctly with the proper tag."""
        footer = Footer("Footer Content")
        self.assertEqual(footer.tag, "footer")
        rendered = footer.render()
        self.assertTrue(rendered.startswith("<footer"))
        self.assertTrue(rendered.endswith("</footer>"))
        self.assertIn("Footer Content", rendered)

    def test_horizontal_rule_render(self):
        """Test that HorizontalRule renders as a self-closing tag with the proper tag."""
        hr = HorizontalRule()
        self.assertEqual(hr.tag, "hr")
        self.assertTrue(hr.self_closing)
        rendered = hr.render()
        self.assertTrue(rendered.startswith("<hr"))
        self.assertTrue(rendered.endswith(" />"), msg=f"Rendered HR: {rendered}")

    def test_main_render(self):
        """Test that Main renders correctly with the proper tag."""
        main = Main("Main Content")
        self.assertEqual(main.tag, "main")
        rendered = main.render()
        self.assertTrue(rendered.startswith("<main"))
        self.assertTrue(rendered.endswith("</main>"))
        self.assertIn("Main Content", rendered)
