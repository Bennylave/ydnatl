from core.tag import HTMLTag


class UnorderedList(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "ul"})

    @staticmethod
    def with_items(*items):
        pass
        # for item in items:
        #     self.add_child(item)
        # return self


class OrderedList(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "ol"})

    @staticmethod
    def with_items(*items):
        pass
        # for item in items:
        #     self.add_child(item)
        # return self


class ListItem(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "li"})


class Datalist(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "datalist"})


class DescriptionDetails(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "dd"})


class DescriptionList(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "dl"})


class DescriptionTerm(HTMLTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "tag": "dt"})