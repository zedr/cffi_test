import unittest

from cffi_test.vectors import UInt32Array as Array, Uint32Range as Range


class RangeTests(unittest.TestCase):
    def test_array_length(self):
        self.assertEqual(len(Array(10)), 10)

    def test_array_indexing(self):
        arr = Array(100)
        arr[42] = 42
        self.assertEqual(arr[42], 42)
        self.assertEqual(arr[0], 0)

    def test_zero_filled_array_iteration(self):
        arr = Array(10)
        self.assertEqual(
            list([0] * 10),
            list(arr)
        )

    def test_array_sum(self):
        arr = Array(10)
        for idx in range(10):
            arr[idx] = idx
        self.assertEqual(arr.sum(), 45)

    def test_negative_indexing(self):
        arr = Array(10)
        arr[9] = 42
        arr[8] = 41
        self.assertEqual(arr[9], arr[-1])
        self.assertEqual(arr[8], arr[-2])
        self.assertRaises(IndexError, lambda: arr[-100])

    def test_out_of_bounds_indexing(self):
        self.assertRaises(IndexError, lambda: Array(10)[100])

    def test_range(self):
        self.assertEqual(list(Range(10)), list(range(10)))
