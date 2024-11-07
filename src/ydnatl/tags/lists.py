from src.ydnatl.core.element import HTMLElement


class UnorderedList(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "ul"})

    @staticmethod
    def with_items(*items):
        pass
        # for item in items:
        #     self.add_child(item)
        # return self


class OrderedList(HTMLElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "ol"})

    @staticmethod
    def with_items(*items):
        pass
        # for item in items:
        #     self.add_child(item)
        # return self


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