import os

import cffi

_here = os.path.dirname(__file__)
_root = os.path.dirname(_here)
_c_source_path = os.path.join(_root, "src", "c_ext")


def c_src(fname):
    with open(os.path.join(_c_source_path, fname)) as fd:
        return fd.read()


ffi = cffi.FFI()
ffi.set_source("cffi_test._utils", c_src("utils.c"))
ffi.cdef(c_src("utils.h"))

if __name__ == "__main__":
    ffi.compile()
