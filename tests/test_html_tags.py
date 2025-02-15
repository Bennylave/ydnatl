import unittest

from src.ydnatl.tags.html import (
    HTML,
    Head,
    Body,
    Title,
    Meta,
    Link,
    Script,
    Style,
)


class TestHTMLTags(unittest.TestCase):

    def test_html_defaults(self):
        """Test that the HTML element sets the proper tag and default attributes."""
        html = HTML("Content")
        self.assertEqual(html.tag, "html")
        self.assertIn("prefix", html.attributes)
        self.assertEqual(html.attributes.get("prefix"), "<!DOCTYPE html>")
        self.assertIn("attributes", html.attributes)
        self.assertEqual(
            html.attributes.get("attributes"), {"lang": "en", "dir": "ltr"}
        )
        rendered = html.render()
        self.assertTrue(rendered.startswith("<html"))
        self.assertTrue(rendered.endswith("</html>"))
        self.assertIn("Content", rendered)

    def test_head_render(self):
        """Test that Head sets tag to 'head' and renders its content correctly."""
        head = Head("Meta Info")
        self.assertEqual(head.tag, "head")
        rendered = head.render()
        self.assertTrue(rendered.startswith("<head"))
        self.assertTrue(rendered.endswith("</head>"))
        self.assertIn("Meta Info", rendered)

    def test_body_render(self):
        body = Body("Body Content")
        self.assertEqual(body.tag, "body")
        rendered = body.render()
        self.assertTrue(rendered.startswith("<body"))
        self.assertTrue(rendered.endswith("</body>"))
        self.assertIn("Body Content", rendered)

    def test_title_render(self):
        """Test that Title sets tag to 'title' and renders its content correctly."""
        title = Title("My Page Title")
        self.assertEqual(title.tag, "title")
        rendered = title.render()
        self.assertTrue(rendered.startswith("<title"))
        self.assertTrue(rendered.endswith("</title>"))
        self.assertIn("My Page Title", rendered)

    def test_meta_render(self):
        """Test that Meta sets tag to 'meta' and renders as self-closing when specified."""
        meta = Meta(self_closing=True, charset="UTF-8")
        self.assertEqual(meta.tag, "meta")
        rendered = meta.render()
        self.assertTrue(rendered.endswith(" />"), msg=f"Rendered meta: {rendered}")
        self.assertIn('charset="UTF-8"', rendered)

    def test_link_render(self):
        """Test that Link sets tag to 'link' and renders as self-closing when specified."""
        link = Link(self_closing=True, rel="stylesheet", href="styles.css")
        self.assertEqual(link.tag, "link")
        rendered = link.render()
        self.assertTrue(rendered.endswith(" />"), msg=f"Rendered link: {rendered}")
        self.assertIn('rel="stylesheet"', rendered)
        self.assertIn('href="styles.css"', rendered)

    def test_script_render(self):
        """Test that Script sets tag to 'script' and renders its content correctly."""
        script = Script("console.log('Hello');")
        self.assertEqual(script.tag, "script")
        rendered = script.render()
        self.assertTrue(rendered.startswith("<script"))
        self.assertTrue(rendered.endswith("</script>"))
        self.assertIn("console.log('Hello');", rendered)

    def test_style_render(self):
        """Test that Style sets tag to 'style' and renders its content correctly."""
        style = Style("body { margin: 0; }")
        self.assertEqual(style.tag, "style")
        rendered = style.render()
        self.assertTrue(rendered.startswith("<style"))
        self.assertTrue(rendered.endswith("</style>"))
        self.assertIn("body { margin: 0; }", rendered)
