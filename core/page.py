class Page:
    def __init__(self, **kwargs):
        self._head = None
        self._body = None
        self._title = None
        self._meta = None

        if "head" in kwargs:
            self.head = kwargs["head"]

        if "body" in kwargs:
            self.body = kwargs["body"]

        if "title" in kwargs:
            self.title = kwargs["title"]

        if "meta" in kwargs:
            self.meta = kwargs["meta"]

    def __str__(self):
        return self.render()

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, value):
        self._head = value

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        self._body = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def meta(self):
        return self._meta

    @meta.setter
    def meta(self, value):
        self._meta = value

    def render(self) -> str:
        # Render the meta
        # Render the body
        # Render the head
        pass
