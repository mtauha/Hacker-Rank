#! /usr/bin/env python3
from itertools import combinations_with_replacement


def Combinations_With_Replacement(str_input,length):
    length = int(length)

    output = sorted(["".join(sorted(x)) for x in combinations_with_replacement(str_input, length)],key=lambda x: (len(x),x))

    return output if output[0] != "" else output[1:]


if __name__ == "__main__":
    str_input, length = input().split()
    Combinations_With_Replacement(str_input=str_input,length=length)