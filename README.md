# YDNATL 

YDNATL is a Python library that lets you build HTML docs using simple classes. It's great for apps that need HTML generation, so you can skip the hassle of writing HTML by hand or using a templating engine.

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://buymeacoffee.com/underwulf)

## Requirements 

Python `3.8` or higher is recommended

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

- Declarative syntax for building HTML documents (like Flutter)
- Easy to read and write
- Supports all HTML5 elements
- Automatically generates unique IDs for elements
- Event callbacks
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
from django.http import HttpResponse
from ydnatl import *

def index(request):
    return HttpResponse(HTML(
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
                Paragraph("This is a paragraph."),
                Paragraph("This is another paragraph.")
            )
        )
    ))
```

### Flask

```python
from flask import Flask
from ydnatl import *

app = Flask(__name__)

@app.route("/")
def index():
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

## Test Coverage 

YDNATL has `100% test coverage`. To run the tests locally, use:

```shell
python -m unittest discover src/ydnatl/tests
```

or:

```shell
python run_test.py
```

## Element Methods: 

- `instance.prepend()`
- `instance.append()`
- `instance.filter()`
- `instance.remove_all()`
- `instance.clear()`
- `instance.pop()`
- `instance.first()`
- `instance.last()`
- `instance.add_attribute()`
- `instance.remove_attribute()`
- `instance.get_attribute()`
- `instance.has_attribute()`
- `instance.generate_id()`
- `instance.clone()`
- `instance.find_by_attribute()`
- `instance.get_attributes()`
- `instance.count_children()`
- `instance.render()`

## Events 

- `instance.on_load()`
- `instance.on_before_render()`
- `instance.on_after_render()`
- `instance.on_unload()`

## Element Properties

- `instance.tag`
- `instance.children`
- `instance.text`
- `instance.attributes`
- `instance.self_closing`

## Modules

| **Module**         	| **Purpose**                       	| **Examples** 	|
|--------------------	|-----------------------------------	|--------------	|
| ydnatl.tags.form   	| Common HTML form elements         	| Examples     	|
| ydnatl.tags.html   	| Structural HTML document elements 	| Examples     	|
| ydnatl.tags.layout 	| Layout related HTML tags          	| Examples     	|
| ydnatl.tags.lists  	| HTML list elements                	| Examples     	|
| ydnatl.tags.media  	| Media related HTML elements       	| Examples     	|
| ydnatl.tags.table  	| HTML table elements               	| Examples     	|
| ydnatl.tags.text   	| HTML text elements                	| Examples     	|

#### ydnatl.tags.form

- `Form()`
- `Input()`
- `Label()`
- `Select()`
- `Option()`
- `Button()`
- `Fieldset()`
- `Optgroup()`

#### ydnatl.tags.html

- `HTML()`
- `Head()`
- `Body()`
- `Title()`
- `Meta()`
- `Link()`
- `Script()`
- `Style()`
- `IFrame()`

#### ydnatl.tags.layout 

- `Div()`
- `Section()`
- `Header()`
- `Nav()`
- `Footer()`
- `HorizontalRule()`
- `Main()`

#### ydnatl.tags.lists

- `OrderedList()`
- `ListItem()`
- `Datalist()`
- `DescriptionDetails()`
- `DescriptionList()`
- `DescriptionTerm()`

#### ydnatl.tags.media

- `Image()`
- `Video()`
- `Audio()`
- `Source()`
- `Picture()`
- `Figure()`
- `Figcaption()`
- `Canvas()`

#### ydnatl.tags.table

- `Table()`
- `TableFooter()`
- `TableHeaderCell()`
- `TableHeader()`
- `TableBody()`
- `TableDataCell()`
- `TableRow()`

#### ydnatl.tags.text

- `H1()`
- `H2()`
- `H3()`
- `H4()`
- `H5()`
- `H6()`
- `Paragraph()`
- `Blockquote()`
- `Pre()`
- `Quote()`
- `Cite()`
- `Em()`
- `Italic()`
- `Span()`
- `Strong()`
- `Abbr()`
- `Link()`
- `Small()`
- `Superscript()`
- `Subscript()`
- `Time()`
- `Code()`

License
-----------------

Please see [LICENSE](https://github.com/sn/ydnatl/blob/master/LICENSE) for licensing details.

Author
-----------------

[github.com/sn](https://github.com/sn) 