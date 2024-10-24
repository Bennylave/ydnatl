from core.tag import HTMLTag


class H1(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "h1"})


class H2(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "h2"})


class H3(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "h3"})


class H4(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "h4"})


class H5(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "h5"})


class H6(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "h6"})


class Paragraph(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "p"})


class Blockquote(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "blockquote"})


class Pre(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "pre"})


class Quote(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "q"})


class Cite(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "cite"})


class Em(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "em"})


class Italic(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "i"})


class Span(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "span"})


class Strong(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "strong"})


class Abbr(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "abbr"})


class Link(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "a"})


class Small(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "small"})


class Superscript(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "sup"})


class Subscript(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "sub"})


class Time(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "time"})


class Code(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "code"})
