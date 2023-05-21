#!/usr/bin/env python

import sys
import timeit

def main():
    print("Testing Native Python range()... ", flush=True)
    t1 = timeit.timeit("sum(range(500))")
    print(t1)

    print("Testing Python Range... ", flush=True)
    t2 = timeit.timeit("Range(500).sum()", setup="from python_test.vectors import Range")
    print(t2)

    print("Testing Cython Range... ", flush=True)
    t2 = timeit.timeit("Range(500).sum()", setup="from cython_test.vectors import Range")
    print(t2)

    print("Testing CFFI Range... ", flush=True)
    t3 = timeit.timeit("Range(500).sum()", setup="from cffi_test.vectors import Range")
    print(t3)

if __name__ == "__main__":
    main()
