class HTMLTag:
    def __init__(self, *args, **kwargs):
        """
        This is the constructor for the Tag class.
        :param args: List of arguments.
        :param kwargs: Keyword arguments.
        """
        self._tag = kwargs.pop("tag", None)

        assert self._tag is not None

        self._children = []
        self._text = ""
        self._attributes = kwargs
        self._self_closing = kwargs.pop("self_closing", False)

        for arg in args:
            if isinstance(arg, HTMLTag):
                self._children.append(arg)
            elif isinstance(arg, str):
                self._text = arg
            elif isinstance(arg, list):
                self._children.extend(arg)
            else:
                raise ValueError(f"Invalid argument type {arg} in Tag or subclass __init__.")

        self.on_load()

    def __del__(self):
        self.on_unload()

    def __str__(self) -> str:
        return self.render()

    def on_load(self):
        """This is a callback method that is called when the tag is loaded."""
        pass

    def on_render(self):
        """This is a callback method that is called when the tag is rendered."""
        pass

    def on_unload(self):
        """This is a callback method that is called when the tag is unloaded."""
        pass

    @property
    def tag(self) -> str:
        return self._tag

    @tag.setter
    def tag(self, value: str) -> None:
        self._tag = value

    @property
    def children(self) -> list:
        return self._children

    @children.setter
    def children(self, value: list) -> None:
        self._children = value

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str) -> None:
        self._text = value

    @property
    def attributes(self) -> dict:
        return self._attributes

    @attributes.setter
    def attributes(self, value: dict) -> None:
        self._attributes = value

    def render(self) -> str:
        """
        This method iteratively renders the tag and its children.
        :return: String representation of the tag and its children.
        """
        parts = [f"<{self.tag}"]
        
        # Re-create this
        for k, v in self.attributes.items():
            if k == "class_name":
                parts.append(f' class="{v}"')
            else:
                parts.append(f' {k}="{v}"')

        if self._self_closing:
            parts.append(" />")
            return "".join(parts)

        parts.append(">")

        if self.text:
            parts.append(self.text)

        if self.children:
            parts.extend(child.render() for child in self.children)

        parts.append(f"</{self.tag}>")

        self.on_render()

        return "".join(parts)
