from core.tag import HTMLTag


class HTML(HTMLTag):
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


class Head(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "head"})


class Body(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "body"})


class Title(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "title"})
