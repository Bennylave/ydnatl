# YDNATL 

YDNATL is a Python library that lets you build HTML docs using simple classes. It's great for apps that need HTML generation or rendering, so you can skip the hassle of writing HTML by hand or using a templating engine.

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://buymeacoffee.com/underwulf)

## Requirements 

Python 3.6 or higher is recommended

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
            Paragraph("This is a test document.")
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
                Paragraph("This is a test document.")
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
                    Paragraph("This is a paragraph.),
                    Paragraph("This is another paragraph.")
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
                    Paragraph("This is a test document.")
                )
            )
        )
    })
```

## Test Coverage 

YDNATL has 100% test coverage. To run the tests locally, use:

```shell
python -m unittest discover src/ydnatl/tests
```

or:

```shell
python run_test.py
```

## Element Methods: 

- Element.prepend
- Element.append
- Element.filter
- Element.remove_all
- Element.clear
- Element.pop
- Element.first
- Element.last 
- Element.add_attribute
- Element.remove_attribute
- Element.get_attribute
- Element.has_attribute
- Element.generate_id
- Element.clone
- Element.find_by_attribute
- Element.get_attributes
- Element.count_children
- Element.render

## Events 

- on_load(element)
- on_before_render(element)
- on_after_render(element)
- on_unload(element)

## Element Properties

- tag
- children
- text
- attributes
- self_closing

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

## Future Features

- Component support 
- More comprehensive examples 
- Relay the render() method to a pure C implementation for speed
- Semantic elements like (BlogPost etc)

License
-----------------

Please see [LICENSE](https://github.com/sn/ydnatl/blob/master/LICENSE) for licensing details.

Author
-----------------

[github.com/sn](https://github.com/sn) 