#!/usr/bin/env python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

def Probability(elements_taken_at_a_time,List,element_to_search_for = 'a'):
    combination = list(combinations(List, elements_taken_at_a_time))
    total_combinations = len(combination)
    a_count = 0

    for i in combination:
        if element_to_search_for in i:
            a_count += 1

    Probability = (a_count/total_combinations)
    return Probability


if __name__ == "__main__":
    
    N = int(input())
    letter_list = input().split()
    K = int(input())
    Probability(K,letter_list)