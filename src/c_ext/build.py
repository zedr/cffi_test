import os

import cffi

_here = os.path.dirname(__file__)


def c_src(fname):
    with open(os.path.join(_here, fname)) as fd:
        return fd.read()


ffi = cffi.FFI()
ffi.set_source("cffi_test._utils", c_src("utils.c"))
ffi.cdef(c_src("utils.h"))

if __name__ == "__main__":
    ffi.compile()
