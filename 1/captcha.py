#!/usr/bin/env python3
ints = list(map(int, input()))
print(sum(a for (a,b) in zip(ints, ints[1:] + [ints[1]]) if a == b))