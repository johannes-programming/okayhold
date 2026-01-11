import unittest
from typing import *

from okayhold.core.OkayDict import OkayDict


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


if __name__ == "__main__":
    unittest.main()
