import unittest
from typing import *

from datahold import core

from okayhold.core.OkayDict import OkayDict
from okayhold.core.OkayList import OkayList
from okayhold.core.OkayObject import OkayObject
from okayhold.core.OkaySet import OkaySet


class TestOkayDict(unittest.TestCase):

    def setUp(self: Self) -> None:
        self.okay_dict = OkayDict({"a": 1, "b": 2})

    def test_contains(self: Self) -> None:
        self.assertIn("a", self.okay_dict)
        self.assertNotIn("c", self.okay_dict)

    def test_getitem(self: Self) -> None:
        self.assertEqual(self.okay_dict["a"], 1)
        with self.assertRaises(KeyError):
            self.okay_dict["c"]

    def test_setitem(self: Self) -> None:
        self.okay_dict["c"] = 3
        self.assertEqual(self.okay_dict["c"], 3)

    def test_delitem(self: Self) -> None:
        del self.okay_dict["a"]
        self.assertNotIn("a", self.okay_dict)

    def test_len(self: Self) -> None:
        self.assertEqual(len(self.okay_dict), 2)

    def test_or(self: Self) -> None:
        merged: Any
        merged = self.okay_dict | {"c": 3}
        self.assertEqual(merged, OkayDict({"a": 1, "b": 2, "c": 3}))


class TestOkayList(unittest.TestCase):

    def setUp(self: Self) -> None:
        self.okay_list = OkayList([1, 2, 3])

    def test_contains(self: Self) -> None:
        self.assertIn(2, self.okay_list)
        self.assertNotIn(5, self.okay_list)

    def test_getitem(self: Self) -> None:
        self.assertEqual(self.okay_list[0], 1)

    def test_setitem(self: Self) -> None:
        self.okay_list[0] = 5
        self.assertEqual(self.okay_list[0], 5)

    def test_append(self: Self) -> None:
        self.okay_list.append(4)
        self.assertEqual(self.okay_list[-1], 4)

    def test_len(self: Self) -> None:
        self.assertEqual(len(self.okay_list), 3)


class TestOkaySet(unittest.TestCase):

    def setUp(self: Self) -> None:
        self.okay_set = OkaySet({1, 2, 3})

    def test_contains(self: Self) -> None:
        self.assertIn(1, self.okay_set)
        self.assertNotIn(4, self.okay_set)

    def test_add(self: Self) -> None:
        self.okay_set.add(4)
        self.assertIn(4, self.okay_set)

    def test_remove(self: Self) -> None:
        self.okay_set.remove(2)
        self.assertNotIn(2, self.okay_set)

    def test_len(self: Self) -> None:
        self.assertEqual(len(self.okay_set), 3)

    def test_union(self: Self) -> None:
        result: Any
        result = self.okay_set | {4, 5}
        self.assertEqual(result, OkaySet({1, 2, 3, 4, 5}))


class TestDoc(unittest.TestCase):
    def test_doc(self: Self) -> None:
        types: tuple[type]
        cls: type
        types = (OkayObject, OkayDict, OkayList, OkaySet)
        for cls in types:
            with self.subTest(name=cls.__name__):
                self.go(cls)

    def go(self: Self, y: type) -> None:
        a: Any
        b: Any
        doc: Any
        error: Any
        name: str
        obj: Any
        name = y.__name__
        for a in dir(y):
            b = getattr(y, a)
            if not callable(b) and not isinstance(b, property):
                continue
            if getattr(b, "__isabstractmethod__", False):
                continue
            if a == "__subclasshook__":
                continue
            doc = getattr(b, "__doc__", None)
            error = "%r inside %r has no docstring" % (a, name)
            self.assertNotEqual(doc, None, error)
        try:
            obj = y()
        except TypeError:
            return
        with self.assertRaises(AttributeError):
            obj.foo = 42


if __name__ == "__main__":
    unittest.main()
