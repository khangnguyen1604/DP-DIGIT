import sys

sys.stdin = open("T4003.inp", "r")
sys.stdout = open("T4003.out", "w")



def get_digit(x):
    v = []
    while x > 0:
        v.append(x % 10)
        x //= 10
    return v

def check_nt(n):
    if (n < 2): return False
    for i in range(2, int(n ** 0.5) + 1):
        if (n % i == 0): return False
    return True

def calc(id, tight, s_even, s_odd, digit, prime, memo):
    if (id < 0): 
        if (s_odd < s_even): return 0
        else: return prime[s_odd - s_even]
    if not tight and memo[id][s_even][s_odd] != -1:
        return memo[id][s_even][s_odd]
    
    cnt = 0
    k = digit[id] if tight else 9

    for i in range(k + 1):
        new_tight = tight and (i == digit[id])
        if id % 2 == 0:
            cnt += calc(id - 1, new_tight, s_even + i, s_odd, digit, prime, memo)
        else:
            cnt += calc(id - 1, new_tight, s_even, s_odd + i, digit, prime, memo)

    if not tight:
        memo[id][s_even][s_odd] = cnt

    return cnt

def solve(a, b):
    memo = [[[-1] * 200 for _ in range(200)] for _ in range(20)]
    prime = [check_nt(i) for i in range(200)]
    digita = get_digit(a - 1)
    digitb = get_digit(b) 
    result = calc(len(digitb) - 1, 1, 0, 0, digitb, prime, memo) - calc(len(digita) - 1, 1, 0, 0, digita, prime, memo)
    print(result)

a, b = map(int, input().split())
solve(a, b)