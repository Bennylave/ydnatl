# ydnatl
from core.page import Page
from tags.html import Body
from tags.layout import Section, Div, Header, Nav
from tags.text import H1, Paragraph, Span, Link
from tags.ui import Button, Form, Input



if __name__ == "__main__":
    home_page = Page(
        title="My Page",
        meta={},
        body=Body(
            H1("Hello, World!"),
            Paragraph("This is a paragraph"),
            Span("This is a span"),
            Section(
                Div(
                    H1("Hello, World!"),
                    Paragraph("This is a paragraph"),
                ),
                Div(
                    Button("Click me!"),
                ),
            ),
        ),
    )

    hero = Section(
            Header(
                Link("Home", href="/"),
                Nav(
                    Link("About", href="/about"),
                    Link("Contact", href="/contact"),
                    Link("Services", href="/services"),
                )
            ),
            H1("Hello, World!"),
            Paragraph("This is a paragraph"),
            Span("This is a span"),
            Section(
                Div(
                    H1("Hello, World!"),
                    Paragraph("This is a paragraph"),
                ),
                Div(Button("Click me!")),
            ),
            Link("Click me!", href="https://www.google.com", target="_blank"),
            Form(
                Input(name="email", placeholder="Email"),
                Input(name="name", placeholder="Name"),
                Input(name="number", placeholder="Number"),
                method="POST"
            ),
        Div("alksdjasdklasdkljald")
    )

    # page = HTMLPage()
    # page.template = ""
    # page.title = ""
    # page.og = {}
    # page.meta = {}
    # page.tracking

    y = hero.append(Paragraph("This is a paragraph at the end"))

    # print(y)
    # .append(Paragraph("This is a paragraph in a div"))

    results = hero.filter(lambda e: e.tag == "div", recursive=True)

    print(results)

    # table = Table.from_csv(file)

    print(hero)
