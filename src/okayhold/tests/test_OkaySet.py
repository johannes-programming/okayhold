import unittest
from typing import *

from okayhold.core.OkaySet import OkaySet

__all__ = ["TestOkaySet"]


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


if __name__ == "__main__":
    unittest.main()
