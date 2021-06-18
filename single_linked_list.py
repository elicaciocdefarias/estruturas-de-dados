from typing import Union, Any


class Node:
    def __init__(self, value):
        self.value: Any = value
        self.next: Union[Node, None] = None
