import sys

sys.stdin = open("T4006.inp", "r")
sys.stdout = open("T4006.out", "w")

MOD = int(1e9 + 7)

def add(x, y):
    return (x + y) % MOD

def digit_dp(idx, tight, rem, digits, dp):
    if idx == len(digits):
        return 1 if (rem == 0 and not tight) else 0
    if not tight and dp[idx][rem] != -1:
        return dp[idx][rem]
    
    max_digit = digits[idx] if tight else 9
    cnt = 0
    
    for i in range(max_digit + 1):
        new_tight = tight and (i == digits[idx])
        cnt = add(cnt, digit_dp(idx + 1, new_tight, (rem + i * i) % 3, digits, dp))
    
    if not tight:
        dp[idx][rem] = cnt
    return cnt

def count_divisible_numbers(n):
    digits = list(map(int, n))
    dp = [[-1] * 3 for _ in range(len(digits))]
    return digit_dp(0, True, 0, digits, dp)

n = input()
print(count_divisible_numbers(n))
