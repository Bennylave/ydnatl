from core.tag import HTMLTag


class Textarea(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "textarea"})


class Select(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "select"})

    @staticmethod
    def with_items(*items):
        pass
        # for item in items:
        #     self.add_child(item)
        # return self


class Option(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "option"})


class Button(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "button"})


class Fieldset(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "fieldset"})


class Form(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "form"})


class Input(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "input", "self_closing": True})


class Label(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "label"})


class Optgroup(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "optgroup"})
