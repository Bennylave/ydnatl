# YDNATL 

YDNATL is a Python library that lets you build HTML docs using simple classes. It's great for apps that need HTML generation or rendering, so you can skip the hassle of writing HTML by hand or using a templating engine.

## Installation

```bash
pip install ydnatl
```

## Usage

```python
from ydnatl import *

# Create a simple HTML document
html = HTML(
    Head(
        Title("My Page")
    ),
    Body(
        Div(
            H1("Hello, World!"),
            P("This is a test document.")
        )
    )
)

# Render the HTML document
print(html.render())
```

## Features

- Declarative syntax for building HTML documents
- Easy to read and write
- Supports all HTML5 elements
- Automatically generates unique IDs for elements
- Supports event hooks for each tag
- Supports rendering to string, file, or sending to browser
- Supports cloning of elements
- Supports finding elements by attribute
- Supports getting attributes of elements
- Supports setting attributes of elements
- Supports counting children of elements
- Supports self-closing tags

## Examples

### FastAPI

```python
from fastapi import FastAPI
from ydnatl import *

app = FastAPI()

@app.get("/")
async def root():
    return HTML(
        Head(
            Title("My Page")
        ),
        Body(
            Section(
                H1("Hello, World!"),
                P("This is a test document.")
            )
        )
    )
```

### Django

```python
from django.shortcuts import render
from ydnatl import *


def index(request):
    return render(request, "index.html", {
        "html": HTML(
            Head(
                Title("My Page"),
                Meta(charset="utf-8"),
                Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
                Link(rel="stylesheet", href="style.css"),
                Script(src="script.js")
            ),
            Body(
                Section(
                    H1("Hello, World!"),
                    P("This is a paragraph.),
                    P("This is another paragraph.")
                )
            )
        )
    })
```

### Flask

```python
from flask import Flask, render_template
from ydnatl import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", {
        "html": HTML(
            Head(
                Title("My Page")
            ),
            Body(
                Section(
                    H1("Hello, World!"),
                    P("This is a test document.")
                )
            )
        )
    })
```

## Modules

#### src.ydnatl.tags.form

- Form
- Input
- Label
- Select
- Option
- Button
- Fieldset

#### src.ydnatl.tags.layout

- HTML
- Head
- Body
- Section
- Div

#### src.ydnatl.tags.text

- H1
- H2
- H3
- H4
- H5
- H6
- P
- Span
- Strong
- Em
- Italic
- Cite
- Abbr
- Link












Components:
LoginForm
RegisterForm
ProfileForm

Navigation
Footer

python -m unittest discover
 python -m unittest discover tests


Examples:

- FastAPI
- Django
- Flask
- Login form
- Register form
- Profile form
- Navigation
- Footer
- Header
- Blog
- Article

Event hooks 
Show methods added to each tag 
Render method



<area>
<article>
<aside>
<b>
<base>
<bdi>
<bdo>
<caption>
<col>
<colgroup>
<data>
<del>
<details>
<dfn>
<dialog>
<embed>
<hgroup>
<ins>
<kbd>
<legend>
<map>
<mark>
<meta>
<meter>
<nav>
<noscript>
<object>
<option>
<output>
<progress>
<summary>
<template>
<track>
<u>
<var>


# class TestMainTag(unittest.TestCase):
#     def test_tag_initialization(self):
#         tag = HTMLTag("Hello", tag="p")
#         self.assertEqual(tag.tag, "p")
#         self.assertEqual(tag.text, "Hello")
#         self.assertEqual(tag.children, [])
#         self.assertEqual(tag.attributes, {})

#     def test_tag_render(self):
#         tag = HTMLTag("Hello", tag="p")
#         self.assertEqual(tag.render(), "<p>Hello</p>")

#     def test_tag_with_children(self):
#         child1 = HTMLTag("Child 1", tag="span")
#         child2 = HTMLTag("Child 2", tag="span")
#         parent = HTMLTag([child1, child2], tag="div")
#         self.assertEqual(parent.render(), "<div><span>Child 1</span><span>Child 2</span></div>")


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
