import unittest
from typing import *


from okayhold.core.OkayList import OkayList


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


if __name__ == "__main__":
    unittest.main()
