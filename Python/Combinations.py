#! /usr/bin/env python3
from itertools import combinations

def Combinations(S,k):
    k = int(k)

    output = sorted(
        ["".join(sorted(x)) for r in range(k+1) for x in combinations(S, r)],
        key=lambda x: (len(x), x),
    )


    return output if output[0] != "" else output[1:]


if __name__ == "__main__":
    
    S, k = input().split()
    Combinations(S=S,k=k)