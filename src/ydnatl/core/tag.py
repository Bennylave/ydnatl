class HTMLElement:
    def __init__(self, *args, tag=None, self_closing=False, **attributes):
        self._tag = tag
        assert self._tag, "Tag name is required"
        self._children = []
        self._text = ""
        self._attributes = attributes
        self._self_closing = self_closing

        for arg in args:
            self._add_child(arg)

        self.on_load()

    def __del__(self):
        self.on_unload()

    def __str__(self) -> str:
        return self.render()

    def _add_child(self, arg):
        """Helper to add children in both prepend and append."""
        if isinstance(arg, HTMLElement):
            self._children.append(arg)
        elif isinstance(arg, str):
            self._text = arg
        elif isinstance(arg, list):
            self._children.extend(arg)
        else:
            raise ValueError(f"Invalid argument type {arg}")

    def prepend(self, *args):
        """ This method prepends children to the current tag. """
        for arg in args:
            self._add_child(arg)
            if isinstance(arg, list):
                self._children = arg + self._children
            else:
                self._children.insert(0, arg)
        return args

    def append(self, *args):
        """ This method appends children to the current tag. """
        for arg in args:
            self._add_child(arg)
        return args

    def filter(self, condition: callable, recursive=False) -> list:
        """ This method filters the children of the current tag. """
        return [child for child in self._children if condition(child)] + (
            [desc for child in self._children for desc in child.filter(condition, recursive=True)] if recursive else []
        )

    def remove_all(self, condition: callable):
        """ This method removes all children that meet the condition. """
        for child in self.filter(condition):
            self._children.remove(child)

    def pop(self, index: int):
        """ This method pops a child from the tag. """
        return self._children.pop(index)

    def first(self):
        """ This method returns the first child of the tag. """
        return self._children[0] if self._children else None

    def last(self):
        """ This method returns the last child of the tag. """
        return self._children[-1] if self._children else None

    def add_attribute(self, key: str, value: str):
        """ This method adds an attribute to the current tag. """
        self._attributes[key] = value

    def remove_attribute(self, key: str):
        """ This method removes an attribute from the current tag. """
        self._attributes.pop(key, None)

    def get_attribute(self, key: str):
        """ This method gets an attribute from the current tag. """
        return self._attributes.get(key)

    def has_attribute(self, key: str):
        """ This method checks if an attribute exists in the current tag. """
        return key in self._attributes

    def generate_id(self):
        """ This method generates an id for the current tag. """
        import uuid

        if "id" not in self._attributes:
            self._attributes["id"] = f"el-{str(uuid.uuid4())[0:6]}"

    def clone(self):
        """ This method clones the current tag. """
        import copy
        return copy.deepcopy(self)

    def find_by_attribute(self, attr_name, attr_value):
        """ This method finds a child by an attribute. """
        for child in self._children:
            if child.get_attribute(attr_name) == attr_value:
                return child
            nested_result = child.find_by_attribute(attr_name, attr_value)
            if nested_result:
                return nested_result
        return None

    def get_attributes(self, *keys) -> dict:
        """ This method returns the attributes of the current tag. """
        return {key: self._attributes.get(key) for key in keys} if keys else self._attributes

    def count_children(self):
        """ This method returns the number of children in the current tag. """
        return len(self._children)

    def on_load(self):
        """ This is a callback method that is called when the tag is loaded. """
        pass

    def on_before_render(self):
        """ This is a callback method that is called before the tag is rendered. """
        pass

    def on_after_render(self):
        """ This is a callback method that is called after the tag is rendered. """
        pass

    def on_unload(self):
        """ This is a callback method that is called when the tag is unloaded. """
        pass

    @property
    def tag(self) -> str:
        return self._tag

    @tag.setter
    def tag(self, value: str) -> None:
        self._tag = value

    @property
    def children(self) -> list:
        return self._children or []

    @property
    def self_closing(self) -> bool:
        return self._self_closing

    @children.setter
    def children(self, value: list) -> None:
        self._children = value

    @property
    def text(self) -> str:
        return self._text or ""

    @text.setter
    def text(self, value: str) -> None:
        self._text = value

    @property
    def attributes(self) -> dict:
        return self._attributes or {}

    @attributes.setter
    def attributes(self, value: dict) -> None:
        self._attributes = value

    def render(self) -> str:
        self.on_before_render()

        attributes = " ".join(
            f'{k if k != "class_name" else "class"}="{v}"' for k, v in self.attributes.items()
        )

        tag_start = f"<{self.tag} {attributes}".strip()

        if self._self_closing:
            result = f"{tag_start} />"
        else:
            children = ''.join(child.render() for child in self._children) if self._children else ""
            result = f"{tag_start}>{self._text or ''}{children}</{self.tag}>"

        self.on_after_render()

        return result
