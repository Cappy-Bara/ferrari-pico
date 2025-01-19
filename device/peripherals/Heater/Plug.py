class Plug:
    def __init__(self, isPlugged) -> None:
        self.isPlugged = isPlugged

    def reverseState(self) -> None:
        self.isPlugged = not self.isPlugged