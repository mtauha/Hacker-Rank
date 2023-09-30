def nonDivisibleSubset(k, s):
    remainder_count = [0] * k
    result = 0
    
    for num in s:
        remainder_count[num % k] += 1
        
    if remainder_count[0] > 0:
        result += 1
    
    for i in range(1, k // 2 + 1):
        if i != k - i:
            result += max(remainder_count[i], remainder_count[k - i])
        else:
            result += 1
    
    return result



if __name__ == '__main__':
    array = [1,2,3,4,5]
    k = 3

    print(nonDivisibleSubset(k=3,s=array))