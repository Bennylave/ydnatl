from src.ydnatl.core.element import HTMLElement


class HTML(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{
            **kwargs,
            "tag": "html",
            "prefix": "<!DOCTYPE html>",
            "attributes": {
                "lang": "en",
                "dir": "ltr"
            }
        })


class Head(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "head"})


class Body(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "body"})


class Title(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "title"})


class Meta(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "meta"})


class Link(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "link"})


class Script(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "script"})


class Style(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "style"})
        
