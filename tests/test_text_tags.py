import unittest

from src.ydnatl.tags.text import (
    H1, H2, H3, H4, H5, H6,
    Paragraph, Blockquote, Pre, Quote, Cite,
    Em, Italic, Span, Strong, Abbr, Link,
    Small, Superscript, Subscript, Time, Code,
)

class TestTextElements(unittest.TestCase):
    def test_text_elements_render(self):
        elements = [
            (H1, "h1", "Header1"),
            (H2, "h2", "Header2"),
            (H3, "h3", "Header3"),
            (H4, "h4", "Header4"),
            (H5, "h5", "Header5"),
            (H6, "h6", "Header6"),
            (Paragraph, "p", "Paragraph text"),
            (Blockquote, "blockquote", "Blockquote text"),
            (Pre, "pre", "Preformatted text"),
            (Quote, "q", "Short quote"),
            (Cite, "cite", "Citation text"),
            (Em, "em", "Emphasized text"),
            (Italic, "i", "Italic text"),
            (Span, "span", "Span text"),
            (Strong, "strong", "Strong text"),
            (Abbr, "abbr", "Abbreviation"),
            (Link, "a", "Link text"),
            (Small, "small", "Small text"),
            (Superscript, "sup", "Superscript text"),
            (Subscript, "sub", "Subscript text"),
            (Time, "time", "Time text"),
            (Code, "code", "Code snippet"),
        ]
        
        for element_class, expected_tag, sample_text in elements:
            with self.subTest(element=element_class.__name__):
                element = element_class(sample_text)
                self.assertEqual(element.tag, expected_tag)
                rendered = element.render()
                self.assertTrue(
                    rendered.startswith(f"<{expected_tag}"),
                    f"Rendered output for {element_class.__name__} should start with <{expected_tag}>."
                )
                self.assertTrue(
                    rendered.endswith(f"</{expected_tag}>"),
                    f"Rendered output for {element_class.__name__} should end with </{expected_tag}>."
                )
                self.assertIn(sample_text, rendered)

