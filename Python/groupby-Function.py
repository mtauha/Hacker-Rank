#!/usr/bin/env python3
from itertools import groupby

S = input()

groups = groupby(S)

for char, group in groups:
    count = len(list(group))
    print(f"({count}, {char})")