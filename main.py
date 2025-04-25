import asyncio
from src.ydnatl.tags.html import Body, HTML, Head, Title
from src.ydnatl.tags.layout import Section, Div, Header, Nav
from src.ydnatl.tags.text import H1, Paragraph, Span, Link
# from src.ydnatl.tags.ui import Button, Form, Input
from src.ydnatl.tags.lists import OrderedList


if __name__ == "__main__":
    # items = [{"text": "This is a paragraph"}, {"text": "This is a paragraph"}, {"text": "This is a paragraph"}]
    
    # b = Body(
    #         H1("Hello, World!"),
    #         Paragraph("This is a paragraph"),
    #         Span("This is a span"),
    #         Section(
    #             [Div(item["text"]) for item in items],
    #             Div(
    #                 H1("Hello, World!"),
    #                 Paragraph("This is a paragraph"),
    #             ),
    #             Div(
    #                 # Button("Click me!"),
    #                 Div(
    #                     Link("Click me!", href="https://www.google.com", target="_blank"),
    #                 )
    #             ),
    #         ),
    #     )
    
    # print(b.render())
    
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

    # Render the HTML document
    # print(html.render())    
    
    # async def x():
    #     result = await b.render()
    #     print(result)
        
    # asyncio.run(x())
    
    
    # async def main():
    #     result = await b.render()
    #     print(result)
        
# main()
    
    # x = b.filter(lambda e: e.tag == "div")
    
    # print(b.render())
    
    # print(x)

    # home_page = Page(
    #     title="My Page",
    #     meta={},
    #     body=Body(
    #         H1("Hello, World!"),
    #         Paragraph("This is a paragraph"),
    #         Span("This is a span"),
    #         Section(
    #             # [Div(item.text) for item in items],
    #             Div(
    #                 H1("Hello, World!"),
    #                 Paragraph("This is a paragraph"),
    #             ),
    #             Div(
    #                 Button("Click me!"),
    #             ),
    #         ),
    #     ),
    # )

    # hero = Section(
    #     Header(
    #         Link("Home", href="/"),
    #         Nav(
    #             Link("About", href="/about"),
    #             Link("Contact", href="/contact"),
    #             Link("Services", href="/services"),
    #         ),
    #     ),
    #     H1("Hello, World!"),
    #     Paragraph("This is a paragraph"),
    #     Span("This is a span"),
    #     Section(
    #         Div(
    #             H1("Hello, World!"),
    #             Paragraph("This is a paragraph"),
    #         ),
    #         Div(Button("Click me!")),
    #     ),
    #     Link("Click me!", href="https://www.google.com", target="_blank"),
    #     Form(
    #         Input(name="email", placeholder="Email"),
    #         Input(name="name", placeholder="Name"),
    #         Input(name="number", placeholder="Number"),
    #         method="POST",
    #         action="/submit",
    #         charset="utf-8",
    #     ),
    #     # Div("alksdjasdklasdkljald", data={
    #     #     "key": "value"
    #     # })
    # )
    
    # para = Paragraph("This is a paragraph")
    # para.append(Span("This is a span"))
    # para.append(Link("This is a link", href="https://www.google.com"))
    # # para.append(Span("This is a span"))
    # # para.append(Span("This is a span"))
    # # para.append(Span("This is a span"))
    # print(para.render())

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

    # div = Div.from_string("<div>Hello, World!</div>")

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

    # y = hero.append(Paragraph("This is a paragraph at the end"))

    # print(hero.render())

    # print(y)
    # .append(Paragraph("This is a paragraph in a div"))

    # divs = hero.filter(lambda e: e.tag == "div", recursive=True)
    #
    # print(divs)

    # table = Table.from_csv(file)

    # print(hero)
    #
    # def fs(value):
    #     return f"{value}em"


    # from src.ydnatl.core.css import CSS
    # from src.ydnatl.core.css import Reset

    # base_css = Reset()

    # hero = CSS("hero", backgroundColor="red", color="blue")

    # css = CSS(
    #     backgroundColor="asdasd",
    #     color="red",
    #     fontSize=12 / 123,
    #     fontWeight="bold"
    # )
    # css.backgroundColor = "blue"
    # css.selector = "#hero"





    # for i in sizes{
    #     css = CSS(
    #         fontSize=fs(i)
    #     )
    # }

    # css.append(hero)
    # css.append(hero)

    # header = Header()
    # body = body
    #
    # Page(header, body, footer).render()






    # class Component:
    #     def __init__(self, html, css):
    #         self.html = html
    #         self.css = css
    #
    #     def render(self):
    #         return self.html.render(add_classes=True)


    # print(css)

    # css.save("styles.css")

    # hero = Section()

    # hero = Section(
    #     Header(
    #         Link("Home", href="/"),
    #         Nav(
    #             Link("About", href="/about"),
    #             Link("Contact", href="/contact"),
    #             Link("Services", href="/services"),
    #         ),
    #     ),
    #     H1("Hello, World!"),
    #     Paragraph("This is a paragraph"),
    #     Span("This is a span"),
    #     Section(
    #         Div(
    #             H1("Hello, World!"),
    #             Paragraph("This is a paragraph"),
    #         ),
    #         Div(Button("Click me!")),
    #     ),
    #     Link("Click me!", href="https://www.google.com", target="_blank"),
    #     Form(
    #         Input(name="email", placeholder="Email"),
    #         Input(name="name", placeholder="Name"),
    #         Input(name="number", placeholder="Number"),
    #         method="POST",
    #         action="/submit",
    #         charset="utf-8",
    #     ),
    # )
    
    # ls = OrderedList.with_items("Item 1", "Item 2", "Item 3")
    
    # print(ls.render())
    
    # print(hero.render())
