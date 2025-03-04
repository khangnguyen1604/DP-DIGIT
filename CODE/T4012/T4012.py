import sys

sys.stdin = open("T4012.inp", "r")
sys.stdout = open("T4012.out", "w")

def get_digit(x):
    res = []
    while x > 0:
        res.append(x % 10)
        x //= 10
    return res

def calc(id, tight, total_sum, digits, memo):
    if id < 0:
        return total_sum
    if not tight and memo[id][total_sum] != -1:
        return memo[id][total_sum]
    
    k = digits[id] if tight else 9
    cnt = 0
    
    for i in range(k + 1):
        new_tight = tight and (i == digits[id])
        cnt = (cnt + calc(id - 1, new_tight, total_sum + i, digits, memo)) % (10**9 + 7)
    
    if not tight:
        memo[id][total_sum] = cnt
    
    return cnt

def solve(A, B):
    memo = [[-1] * 165 for _ in range(20)]
    digitA = get_digit(A - 1)
    digitB = get_digit(B)
    
    return (calc(len(digitB) - 1, True, 0, digitB, memo) - calc(len(digitA) - 1, True, 0, digitA, memo)) % (10**9 + 7)

A, B = map(int, input().split())
print(solve(A, B))
