import sys

sys.stdin = open("T4010.inp", "r")
sys.stdout = open("T4010.out", "w")

def get_digit(x):
    res = []
    while x > 0:
        res.append(x % 10)
        x //= 10
    return res

def calc(id, tight, large_0, mask, digit, dp):
    if id < 0:
        return 1
    if not tight and dp[id][mask] != -1:
        return dp[id][mask]
    
    k = digit[id] if tight else 9
    cnt = 0
    for i in range(k + 1):
        new_tight = tight and (i == digit[id])
        new_large_0 = large_0 or (i > 0)
        
        if not new_large_0:
            cnt += calc(id - 1, new_tight, new_large_0, 0, digit, dp)
        elif not ((mask >> i) & 1):
            cnt += calc(id - 1, new_tight, new_large_0, mask | (1 << i), digit, dp)
    
    if not tight:
        dp[id][mask] = cnt
    return cnt

def solve(A, B):
    dp = [[-1] * 1025 for _ in range(20)]
    digitA = get_digit(A - 1)
    digitB = get_digit(B)
    
    return calc(len(digitB) - 1, True, False, 0, digitB, dp) - calc(len(digitA) - 1, True, False, 0, digitA, dp)

A, B = map(int, input().split())
print(solve(A, B))
