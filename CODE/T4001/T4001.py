import sys

sys.stdin = open("T4001.inp", "r")
sys.stdout = open("T4001.out", "w")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_digits(x):
    return list(map(int, str(x)))

def digit_dp(pos, tight, sum_digits, digits, dp, prime):
    if pos == len(digits):
        return 1 if prime[sum_digits] else 0
    if not tight and dp[pos][sum_digits] != -1:
        return dp[pos][sum_digits]
    
    limit = digits[pos] if tight else 9
    count = 0
    for i in range(limit + 1):
        new_tight = tight and (i == digits[pos])
        count += digit_dp(pos + 1, new_tight, sum_digits + i, digits, dp, prime)
    
    if not tight:
        dp[pos][sum_digits] = count
    
    return count

def count_prime_digit_sums(A, B):
    max_digit_sum = 9 * 18  # Maximum sum of digits for a 18-digit number
    prime = [is_prime(i) for i in range(max_digit_sum + 1)]
    
    dp = [[-1] * (max_digit_sum + 1) for _ in range(20)]
    digits_B = get_digits(B)
    count_B = digit_dp(0, True, 0, digits_B, dp, prime)
    
    dp = [[-1] * (max_digit_sum + 1) for _ in range(20)]
    digits_A = get_digits(A - 1)
    count_A = digit_dp(0, True, 0, digits_A, dp, prime)
    
    return count_B - count_A

A, B = map(int, input().split())
print(count_prime_digit_sums(A, B))
