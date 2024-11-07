# ydnatl
from src.ydnatl.core.page import Page
from src.ydnatl.tags.html import Body
from src.ydnatl.tags.layout import Section, Div, Header, Nav
from src.ydnatl.tags.text import H1, Paragraph, Span, Link
from src.ydnatl.tags.ui import Button, Form, Input

# from src.ydnatl.tags.page import HTML
# from src.ydnatl.core.html import Partial

if __name__ == "__main__":
    items = []

    home_page = Page(
        title="My Page",
        meta={},
        body=Body(
            H1("Hello, World!"),
            Paragraph("This is a paragraph"),
            Span("This is a span"),
            Section(
                # [Div(item.text) for item in items],
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
            ),
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
            method="POST",
            action="/submit",
            charset="utf-8",
        ),
        # Div("alksdjasdklasdkljald", data={
        #     "key": "value"
        # })
    )

    # html = HTML(Body(
    #     H1("hello world"),
    #     Paragraph("this is a paragraph"),
    # ))
    #
    # if user.is_authed():
    #     html.append(Section(f"Welcome back! {user.email}"))
    #
    # html.append(Partial("footer.html"))

    # heaer = Header.load_from_file("header.html")

    # user_partial = Partial(
    #     Div(f"Welcome back! {user.email}")
    # )

    # def create_form():
    #     return Form(method="POST").append(
    #         Input(name="email", placeholder="Email", value=user.email),
    #         Input(name="name", placeholder="Name", value=user.name),
    #         Input(name="number", placeholder="Number"),
    #         Button("Submit")
    #     )

    # newsletter_partial = Partial(
    #     Form(
    #         Paragraph("Subscribe to our newsletter"),
    #         Input(name="email", placeholder="Email"),
    #         Button("Subscribe")
    #     )
    # )

    # hero.append(partial)

    div = Div.from_string("<div>Hello, World!</div>")

    # https://chatgpt.com/c/6721f16e-5478-8008-a525-2bcf1280022b

    # @staticmethod
    # def from_string(string: str):
    #     """ This method loads the content of a string. """
    #     import xml.etree.ElementTree as ET
    #     element = ET.fromstring(string)
    #     return HTMLElement._from_etree_element(element)
    #
    #
    # @staticmethod
    # def _from_etree_element(element):
    #     tag = element.tag
    #     attributes = element.attrib
    #     children = [HTMLElement._from_etree_element(child) for child in element]
    #     text = element.text or ""
    #
    #     html_element = HTMLElement(tag=tag, **attributes)
    #     html_element._children = children
    #     html_element._text = text.strip()
    #
    #     return html_element
    # html.append()

    # body = Body().append(H1("Hello World!"))

    # page = HTMLPage()
    # page.template = ""
    # page.title = ""
    # page.og = {}
    # page.meta = {}
    # page.tracking

    y = hero.append(Paragraph("This is a paragraph at the end"))

    # print(y)
    # .append(Paragraph("This is a paragraph in a div"))

    divs = hero.filter(lambda e: e.tag == "div", recursive=True)

    print(divs)

    # table = Table.from_csv(file)

    print(hero)
