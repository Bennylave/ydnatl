import unittest

from src.ydnatl.tags.ui import (
    Textarea,
    Select,
    Option,
    Button,
    Fieldset,
    Form,
    Input,
    Label,
    Optgroup,
)


class TestFormElements(unittest.TestCase):

    def test_textarea_render(self):
        """Test that Textarea renders correctly with the proper tag and content."""
        ta = Textarea("Sample text")
        self.assertEqual(ta.tag, "textarea")
        rendered = ta.render()
        self.assertTrue(rendered.startswith("<textarea"), msg=f"Rendered: {rendered}")
        self.assertTrue(rendered.endswith("</textarea>"), msg=f"Rendered: {rendered}")
        self.assertIn("Sample text", rendered)

    def test_select_with_items(self):
        """
        Test the static with_items method of Select.
        Note: According to the implementation, Select.with_items returns an Option element
        with the provided items appended as children.
        """
        result = Select.with_items("Option 1", "Option 2")
        self.assertEqual(result.tag, "select")
        self.assertEqual(len(result.children), 2)
        rendered = result.render()
        self.assertIn("Option 1", rendered)
        self.assertIn("Option 2", rendered)

    def test_option_render(self):
        """Test that Option renders correctly with the proper tag and content."""
        opt = Option("Option text")
        self.assertEqual(opt.tag, "option")
        rendered = opt.render()
        self.assertTrue(rendered.startswith("<option"), msg=f"Rendered: {rendered}")
        self.assertTrue(rendered.endswith("</option>"), msg=f"Rendered: {rendered}")
        self.assertIn("Option text", rendered)

    def test_button_render(self):
        """Test that Button renders correctly with the proper tag and content."""
        btn = Button("Click me")
        self.assertEqual(btn.tag, "button")
        rendered = btn.render()
        self.assertTrue(rendered.startswith("<button"), msg=f"Rendered: {rendered}")
        self.assertTrue(rendered.endswith("</button>"), msg=f"Rendered: {rendered}")
        self.assertIn("Click me", rendered)

    def test_fieldset_render(self):
        """Test that Fieldset renders correctly with the proper tag and content."""
        fs = Fieldset("Fieldset content")
        self.assertEqual(fs.tag, "fieldset")
        rendered = fs.render()
        self.assertTrue(rendered.startswith("<fieldset"), msg=f"Rendered: {rendered}")
        self.assertTrue(rendered.endswith("</fieldset>"), msg=f"Rendered: {rendered}")
        self.assertIn("Fieldset content", rendered)

    def test_form_render(self):
        """Test that Form renders correctly with the proper tag and content."""
        form = Form("Form content")
        self.assertEqual(form.tag, "form")
        rendered = form.render()
        self.assertTrue(rendered.startswith("<form"), msg=f"Rendered: {rendered}")
        self.assertTrue(rendered.endswith("</form>"), msg=f"Rendered: {rendered}")
        self.assertIn("Form content", rendered)

    def test_input_render(self):
        """Test that Input renders as a self-closing tag with the proper tag."""
        inp = Input()
        self.assertEqual(inp.tag, "input")
        self.assertTrue(inp.self_closing)
        rendered = inp.render()
        self.assertTrue(rendered.startswith("<input"), msg=f"Rendered: {rendered}")
        self.assertTrue(rendered.endswith(" />"), msg=f"Rendered: {rendered}")

    def test_label_render(self):
        """Test that Label renders correctly with the proper tag and content."""
        lbl = Label("Label text")
        self.assertEqual(lbl.tag, "label")
        rendered = lbl.render()
        self.assertTrue(rendered.startswith("<label"), msg=f"Rendered: {rendered}")
        self.assertTrue(rendered.endswith("</label>"), msg=f"Rendered: {rendered}")
        self.assertIn("Label text", rendered)

    def test_optgroup_render(self):
        """Test that Optgroup renders correctly with the proper tag and content."""
        og = Optgroup("Group text")
        self.assertEqual(og.tag, "optgroup")
        rendered = og.render()
        self.assertTrue(rendered.startswith("<optgroup"), msg=f"Rendered: {rendered}")
        self.assertTrue(rendered.endswith("</optgroup>"), msg=f"Rendered: {rendered}")
        self.assertIn("Group text", rendered)
