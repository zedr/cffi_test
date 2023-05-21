import cython


class Range:
    """A range"""
    _arr: cython.int

    def __init__(self, length: cython.int):
        arr: cython.vector[cython.int] = []
        i: cython.int = 0
        while i < length:
            arr.append(i)
            i += 1
        self._arr = arr

    def sum(self):
        acc: cython.int = 0
        num: cython.int
        for num in self._arr:
            acc += num
        return acc

