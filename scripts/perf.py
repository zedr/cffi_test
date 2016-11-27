#!/usr/bin/env python

import sys
import timeit

def main():
    sys.stdout.write("Testing Python range... ")
    sys.stdout.flush()
    t1 = timeit.timeit("sum(range(500))")
    print(t1)

    sys.stdout.write("Testing CFFI Range... ")
    sys.stdout.flush()
    t2 = timeit.timeit("Range(500).sum()", setup="from cffi_test import Range")
    print(t2)

if __name__ == "__main__":
    main()
