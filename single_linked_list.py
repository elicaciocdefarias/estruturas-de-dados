from typing import Union, Any


class Node:
    def __init__(self, value):
        self.value: Any = value
        self.next: Union[Node, None] = None

    def __str__(self):
        return f"{self.value}"

    def __repr__(self):
        return f"{self.value}"


class SingleLinkedList:
    def __init__(self):
        self.head: Union[Node, None] = None

    def __str__(self):
        items = [str(item.value) for index, item in enumerate(self) if index <= 5]
        string = " -> ".join(items)
        return f"{string}..."

    def __repr__(self):
        items = [str(item.value) for index, item in enumerate(self) if index <= 5]
        string = " -> ".join(items)
        return f"{string}..."

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def __len__(self):
        return len([node for node in self])

    def __getitem__(self, value):
        return self.find(value)

    def add(self, value) -> None:
        node: Node = Node(value)

        if self.head is None:
            self.head = node
            return

        current = None
        for current in self:
            ...
        current.next = node

    def remove(self, value) -> None:
        if self.head.value == value:
            self.head = self.head.next
            return

        current = None
        previous = None
        for current in self:
            if current.value == value:
                break
            previous = current
        previous.next = current.next

    def find(self, value) -> Union[Node, None]:
        if self.head is None:
            return
        if self.head.value == value:
            return self.head

        for current in self:
            if current.value == value:
                return current
