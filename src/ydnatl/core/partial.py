from src.ydnatl.core.element import HTMLElement


class Partial(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": None})
