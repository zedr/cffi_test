# noinspection PyUnresolvedReferences
from cffi_test._utils.lib import make_u32a, make_u32r, free, sum_u32a


class UInt32Array(object):
    """An array of uint32_t.
    """
    array_constructor = make_u32a

    def __init__(self, length):
        self._length = length
        self._arr = self.array_constructor(length)

    def __del__(self):
        free(self._arr)
        del (self._arr)

    def __len__(self):
        return self._length

    def __getitem__(self, key):
        if key < 0:
            key = self._length - abs(key)
        if 0 <= key < self._length:
            return self._arr[key]
        else:
            raise IndexError(
                "{0} index out of range".format(type(self).__name__)
            )

    def __setitem__(self, key, value):
        self._arr[key] = value

    def __iter__(self):
        return iter(self._arr[idx] for idx in range(self._length))

    def sum(self):
        return sum_u32a(self._arr, self._length)


class Uint32Range(UInt32Array):
    array_constructor = make_u32r
