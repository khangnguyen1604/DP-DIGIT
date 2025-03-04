import sys

sys.stdin = open("T4011.inp", "r")
sys.stdout = open("T4011.out", "w")

def sieve(limit):
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if prime[i]:
            for j in range(i * i, limit + 1, i):
                prime[j] = False
    return prime

def calc(id, tight, sum_digits, remainder, n, k, prime, dp):
    if id >= len(n):
        return 1 if prime[sum_digits] and remainder == 0 else 0
    
    if not tight and dp[id][sum_digits][remainder] != -1:
        return dp[id][sum_digits][remainder]
    
    max_digit = int(n[id]) if tight else 9
    count = 0
    
    for i in range(max_digit + 1):
        new_tight = tight and (i == int(n[id]))
        count += calc(id + 1, new_tight, sum_digits + i, (remainder * 10 + i) % k, n, k, prime, dp)
    
    if not tight:
        dp[id][sum_digits][remainder] = count
    
    return count

def solve():
    L, R, k = input().split()
    k = int(k)
    prime = sieve(450)
    
    sum_digits = sum(int(d) for d in L)
    remainder = int(L) % k
    
    while len(L) < len(R):
        L = '0' + L
    
    dp = [[[-1] * k for _ in range(455)] for _ in range(55)]
    result = (calc(0, True, 0, 0, R, k, prime, dp) - calc(0, True, 0, 0, L, k, prime, dp)) % (10**9 + 7)
    
    if prime[sum_digits] and remainder == 0:
        result = (result + 1) % (10**9 + 7)
    
    return result

print(solve())
