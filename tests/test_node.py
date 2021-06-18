import pytest
from single_linked_list import Node


@pytest.fixture
def node():
    return Node("head node")


def test_should_have_property_called_value(node):
    assert hasattr(node, "value") is True


def test_should_have_property_called_next(node):
    assert hasattr(node, "next") is True


def test_should_correctly_set_value_value_property(node):
    assert node.value == "head node"


def test_should_have_property_next_with_value_none(node):
    assert node.next is None


def test_should_have_property_next_with_value_other_than_none():
    node = Node("head node")
    next_node = Node("next node")
    node.next = next_node
    assert node.next is not None
