class Range:
    def __init__(self, length: int):
        i = 0
        arr = []
        while i < length:
            arr.append(i)
            i += 1
        self._arr = arr

    def sum(self):
        acc = 0
        for num in self._arr:
            acc += num
        return acc

            
