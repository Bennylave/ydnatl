from core.tag import HTMLElement


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
