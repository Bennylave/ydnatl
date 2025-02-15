from src.ydnatl.core.element import HTMLElement


class Textarea(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "textarea"})


class Select(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "select"})

    @staticmethod
    def with_items(*items, **kwargs):
        opt = Select(**kwargs)
        for item in items:
            if isinstance(item, HTMLElement):
                opt.append(item)
            else:
                opt.append(Option(item))
        return opt


class Option(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "option"})


class Button(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "button"})


class Fieldset(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "fieldset"})


class Form(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "form"})


class Input(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "input", "self_closing": True})


class Label(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "label"})


class Optgroup(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "optgroup"})
