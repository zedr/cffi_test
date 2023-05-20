#!/usr/bin/env python

import sys
import timeit

def main():
    print("Testing Python range... ", flush=True)
    t1 = timeit.timeit("sum(range(500))")
    print(t1)

    print("Testing CFFI Range... ", flush=True)
    t2 = timeit.timeit("Range(500).sum()", setup="from cffi_test import Range")
    print(t2)

if __name__ == "__main__":
    main()
