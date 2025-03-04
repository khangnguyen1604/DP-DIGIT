import sys
import math

sys.stdin = open("T4008.inp", "r")
sys.stdout = open("T4008.out", "w")

def get_digit(x):
    res = []
    while x > 0:
        res.append(x % 10)
        x //= 10
    return res

def calc(id, tight, sum_digits, sum_sqr_digits, digit, dp):
    if id < 0:
        return math.gcd(sum_digits, sum_sqr_digits) == 1
    
    if not tight and dp[id][sum_digits][sum_sqr_digits] != -1:
        return dp[id][sum_digits][sum_sqr_digits]
    
    k = digit[id] if tight else 9
    cnt = 0
    for i in range(k + 1):
        new_tight = tight and (i == digit[id])
        cnt += calc(id - 1, new_tight, sum_digits + i, sum_sqr_digits + i * i, digit, dp)
    
    if not tight:
        dp[id][sum_digits][sum_sqr_digits] = cnt
    return cnt

def solve(A, B):
    digitA = get_digit(A - 1)
    digitB = get_digit(B)
    
    dp = [[[-1] * 1460 for _ in range(165)] for _ in range(20)]
    result = calc(len(digitB) - 1, True, 0, 0, digitB, dp)
    result -= calc(len(digitA) - 1, True, 0, 0, digitA, dp)
    
    print(result)

A, B = map(int, input().split())
solve(A, B)
