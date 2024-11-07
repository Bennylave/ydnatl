class CSS:
    def __init__(self, *args, **kwargs):
        pass

    def x(self):
        return CSS(
            ".orange",
            backgroundColor="orange",
            fontStyle="italic"
        )

    def render(self) -> str:
        pass
