CFFI test
=========
The simplest example of a CFFI powered module I could come up with.

Pre-requisites
--------------
 - cffi
 - gcc

Installation
------------
Just:

    $ pip install .

or use the included Makefile.

Testing
-------
After installing, run:

    make test

Measuring performance gains
---------------------------
You can check how much performance you are getting out of using CFFI with:

    make perf

