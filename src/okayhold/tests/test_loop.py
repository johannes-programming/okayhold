import unittest
from typing import *

from okayhold import core

__all__ = ["TestDoc"]


class TestDoc(unittest.TestCase):
    def test_doc(self: Self) -> None:
        name: str
        s: str
        t: str
        for s in ("Data", "Hold", "Okay"):
            for t in ("Object", "Dict", "List", "Set"):
                name = s + t
                with self.subTest(name=name):
                    self.go(name=name)

    def go(self: Self, name: str) -> None:
        a: Any
        b: Any
        doc: Any
        error: Any
        obj: Any
        y: Any
        y = getattr(getattr(core, name), name)
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
