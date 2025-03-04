import sys

sys.stdin = open("T4014.inp", "r")
sys.stdout = open("T4014.out", "w")

def get_digits(x):
    digits = []
    while x > 0:
        digits.append(x % 10)
        x //= 10
    return digits

def calc(idx, tight, digit_sum, d, digits, dp):
    if idx < 0:
        return 1 if digit_sum == d else 0
    
    if not tight and dp[idx][digit_sum] != -1:
        return dp[idx][digit_sum]
    
    limit = digits[idx] if tight else 9
    count = 0
    
    for i in range(limit + 1):
        new_tight = tight and (i == digits[idx])
        count += calc(idx - 1, new_tight, digit_sum + i, d, digits, dp)
    
    if not tight:
        dp[idx][digit_sum] = count
    
    return count

def solve(a, b, d, dp):
    digits_a = get_digits(a - 1)
    digits_b = get_digits(b)
    return calc(len(digits_b) - 1, True, 0, d, digits_b, dp) - calc(len(digits_a) - 1, True, 0, d, digits_a, dp)


t = int(input())
queries = [tuple(map(int, input().split())) for _ in range(t)]

max_digit_sum = 9 * 19
max_digit_length = 19
dp = [[-1] * (max_digit_sum + 1) for _ in range(max_digit_length)]

results = [0] * (t + 1)
digitM = get_digits(10**19)

for i in range(1, max_digit_sum + 1):
    dp = [[-1] * (max_digit_sum + 1) for _ in range(max_digit_length)]  # Reset memory
    calc(len(digitM) - 1, True, 0, i, digitM, dp)
    for j in range(t):
        a, b = queries[j]
        results[j] += solve((a + i - 1) // i, b // i, i, dp)

for res in results[:-1]:
    print(res)
