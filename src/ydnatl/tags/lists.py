from src.ydnatl.core.element import HTMLElement


class UnorderedList(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "ul"})

    @staticmethod
    def with_items(*items, **kwargs):
        ul = UnorderedList(**kwargs)
        for item in items:
            if isinstance(item, HTMLElement):
                ul.append(item)
            else:
                ul.append(ListItem(item))
        return ul


class OrderedList(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "ol"})

    @staticmethod
    def with_items(*items, **kwargs):
        ol = OrderedList(**kwargs)
        for item in items:
            if isinstance(item, HTMLElement):
                ol.append(item)
            else:
                ol.append(ListItem(item))
        return ol


class ListItem(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "li"})


class Datalist(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "datalist"})


class DescriptionDetails(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "dd"})


class DescriptionList(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "dl"})


class DescriptionTerm(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "dt"})