import sys

sys.stdin = open("T4002.inp", "r")
sys.stdout = open("T4002.out", "w")

def get_digits(x):
    return list(map(int, str(x)))

def digit_dp(idx, tight, number, sumd, digits, k, dp):
    if idx == len(digits):
        return 1 if (number == 0 and sumd == 0) else 0
    if not tight and dp[idx][number][sumd] != -1:
        return dp[idx][number][sumd]
    
    limit = digits[idx] if tight else 9
    cnt = 0
    
    for i in range(limit + 1):
        new_tight = tight and (i == digits[idx])
        cnt += digit_dp(idx + 1, new_tight, (number * 10 + i) % k, (sumd + i) % k, digits, k, dp)
    
    if not tight:
        dp[idx][number][sumd] = cnt
    return cnt

def count_divisible_numbers(A, B, k):
    if k > 162:
        return 0
    
    def count_up_to(x):
        if x < 0:
            return 0
        digits = get_digits(x)
        dp = [[[-1] * k for _ in range(k)] for _ in range(len(digits))]
        return digit_dp(0, True, 0, 0, digits, k, dp)
    
    return count_up_to(B) - count_up_to(A - 1)

A, B, k = map(int, input().split())
print(count_divisible_numbers(A, B, k))
