import unittest
from typing import *

from okayhold.core.OkayDict import OkayDict
from okayhold.core.OkayList import OkayList
from okayhold.core.OkayObject import OkayObject
from okayhold.core.OkaySet import OkaySet


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
        obj: Any
        for a in dir(y):
            b = getattr(y, a)
            if not callable(b) and not isinstance(b, property):
                continue
            if getattr(b, "__isabstractmethod__", False):
                continue
            if a == "__subclasshook__":
                continue
            doc = getattr(b, "__doc__", None)
            error = "%r inside %r has no docstring" % (a, y.__name__)
            self.assertNotEqual(doc, None, error)
        try:
            obj = y()
        except TypeError:
            return
        with self.assertRaises(AttributeError):
            obj.foo = 42


if __name__ == "__main__":
    unittest.main()
