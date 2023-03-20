from testfixtures import compare, Comparison
import unittest


def add(a, b):
    return a+b


def create_object(name, value):
    return {name: value}


class TestIt(unittest.TestCase):
    def test_add(self):
        result = add(2, 3)
        compare(result, 5)

    def test_create_object(self):
        result = create_object(name="dummy-object", value=4)
        compare(result, Comparison(result, name="dummy-object", value=4))

