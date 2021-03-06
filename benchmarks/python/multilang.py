#!/usr/bin/env python3

import math
import sys
import time

def find_first():
    cf = contents.find
    return timer(lambda: cf("en:Benin"))

def timer(f, count=100):
    a = 1e300
    def g():
        return
    for i in range(3):
        start = time.time()
        for j in range(count):
            g()
        a = min(a, (time.time() - start) / count)

    b = 1e300
    for i in range(3):
        start = time.time()
        for j in range(count):
            f()
        b = min(b, (time.time() - start) / count)

    return round(b - a, int(round(math.log(count, 10) - math.log(b - a, 10))))

contents = open('../../tests/text-test-data/yiwiki.xml', 'r').read()

benchmarks = (
    find_first,
    )

to_run = sys.argv[1:]
bms = []
if to_run:
    for r in to_run:
        for b in benchmarks:
            if b.__name__.startswith(r):
                bms.append(b)
else:
    bms = benchmarks

for b in bms:
    sys.stdout.write(b.__name__ + ' ')
    sys.stdout.flush()
    print(b())
