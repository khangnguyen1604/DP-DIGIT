import sys

sys.stdin = open("T4013.inp", "r")
sys.stdout = open("T4013.out", "w")

def get_digits(x):
    digits = []
    while x > 0:
        digits.append(x % 10)
        x //= 10
    return digits

def calc(idx, tight, count_d, digits, d, K, dp):
    if idx < 0:
        return 1 if count_d == K else 0
    
    if not tight and dp[idx][count_d] != -1:
        return dp[idx][count_d]
    
    max_digit = digits[idx] if tight else 9
    count = 0
    
    for i in range(max_digit + 1):
        new_tight = tight and (i == digits[idx])
        count += calc(idx - 1, new_tight, count_d + (i == d), digits, d, K, dp)
    
    if not tight:
        dp[idx][count_d] = count
    
    return count

def solve(A, B, d, K):
    digits_A = get_digits(A - 1)
    digits_B = get_digits(B)
    
    dp = [[-1] * 20 for _ in range(20)]
    count_B = calc(len(digits_B) - 1, True, 0, digits_B, d, K, dp)
    
    dp = [[-1] * 20 for _ in range(20)]
    count_A = calc(len(digits_A) - 1, True, 0, digits_A, d, K, dp)
    
    return count_B - count_A

A, B, d, K = map(int, input().split())
print(solve(A, B, d, K))
