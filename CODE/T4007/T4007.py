import sys

sys.stdin = open("T4007.inp", "r")
sys.stdout = open("T4007.out", "w")

def get_digit(x):
    v = []
    while (x > 0):
        v.append(x % 10)
        x //= 10
    return v

def digit_dp(idx, tight, total, digits, dp):
    if idx == -1:
        return 1 if total == 101 else 0
    if not tight and dp[idx][total] != -1:
        return dp[idx][total]
    
    max_digit = digits[idx] if tight else 9
    cnt = 0
    
    for i in range(max_digit + 1):
        new_tight = tight and (i == digits[idx])
        new_total = total + (i if idx % 2 else -i)
        cnt += digit_dp(idx - 1, new_tight, new_total, digits, dp)
    
    if not tight:
        dp[idx][total] = cnt
    return cnt

def count_special_numbers(A, B):
    dp = [[-1] * 200 for _ in range(20)]
    digitsB = get_digit(B)
    digitsA = get_digit(A - 1)
    return digit_dp(len(digitsB) - 1, True, 100, digitsB, dp) - digit_dp(len(digitsA) - 1, True, 100, digitsA, dp)

A, B = map(int, input().split())
print(count_special_numbers(A, B))
