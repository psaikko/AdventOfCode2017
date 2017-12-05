#!/usr/bin/env python3
ints = list(map(int, input()))
n = len(ints)
print(sum(a for (a,b) in zip(ints, ints[n//2:] + ints[:n//2]) if a == b))