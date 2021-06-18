from single_linked_list import SingleLinkedList


def test_should_have_property_called_head():
    sll = SingleLinkedList()
    assert hasattr(sll, "head")


def test_should_sets_head_node_when_equal_none():
    value = "head node"
    sll = SingleLinkedList()

    sll.add(value)

    assert sll.head.value == value


def test_should_return_str_representaion_correctly():
    sll = SingleLinkedList()

    assert f"{sll}" == "..."


def test_should_return_str_representaion_correctly_1():
    sll = SingleLinkedList()
    sll.add(1)

    assert f"{sll}" == "1..."


def test_should_return_str_representaion_correctly_2():
    sll = SingleLinkedList()
    sll.add(1)
    sll.add(2)

    assert f"{sll}" == "1 -> 2..."


def test_should_add_node_end_list():
    head_node = "head node"
    tail_node = "tail node"

    sll = SingleLinkedList()

    sll.add(head_node)
    sll.add(tail_node)

    assert sll.head.next.value == tail_node


def test_should_remove_node_end_list():
    head_node = "head node"
    tail_node = "tail node"
    sll = SingleLinkedList()
    sll.add(head_node)
    sll.add(tail_node)

    sll.remove(tail_node)

    assert sll.head.next is None


def test_should_remove_node_middle_list():
    head_node = "head node"
    middle_node = "middle node"
    tail_node = "tail node"
    sll = SingleLinkedList()
    sll.add(head_node)
    sll.add(middle_node)
    sll.add(tail_node)

    sll.remove(middle_node)

    assert sll.head.next.value == tail_node


def test_should_remove_node_head_list():
    head_node = "head node"
    tail_node = "tail node"
    sll = SingleLinkedList()
    sll.add(head_node)
    sll.add(tail_node)

    sll.remove(head_node)

    assert sll.head.value == tail_node


def test_should_return_correct_node_1():
    head_node = "head node"
    sll = SingleLinkedList()
    sll.add(head_node)

    result = sll.find(head_node)

    assert result.value == head_node


def test_should_return_correct_node_2():
    head_node = "head node"
    tail_node = "tail node"
    sll = SingleLinkedList()
    sll.add(head_node)
    sll.add(tail_node)

    result = sll.find(tail_node)

    assert result.value == tail_node


def test_should_return_correct_node_3():
    head_node = "head node"
    sll = SingleLinkedList()
    sll.add(head_node)

    result = sll["head node"]

    assert result.value == head_node


def test_should_return_none_1():
    head_node = "head node"
    sll = SingleLinkedList()

    result = sll.find(head_node)

    assert result is None


def test_should_return_none_2():
    head_node = "head node"
    sll = SingleLinkedList()
    sll.add(head_node)

    result = sll.find("tail node")

    assert result is None


def test_should_have_len_equal_zero():
    sll = SingleLinkedList()
    assert len(sll) == 0
