import sys

sys.stdin = open("T4004.inp", "r")
sys.stdout = open("T4004.out", "w")

def get_digit(x):
    v = []
    while (x > 0):
        v.append(x % 10)
        x //= 10
    return v

def calc(id, tight, pre, digit, memo):
    if (id < 0):
        return 1
    if not tight and memo[id][pre] != -1:
        return memo[id][pre]
    cnt = 0
    k = digit[id] if tight else 9
    for i in range(k + 1):
        if (pre != 1) or (i != 3):
            new_tight = tight if (i == digit[id]) else 0
            cnt += calc(id - 1, new_tight, i, digit, memo)
    if tight == 0:
        memo[id][pre] = cnt
    return cnt

def solve(a, b):
    
    digita = get_digit(a - 1)
    digitb = get_digit(b)
    cnt1 = calc(len(digitb) - 1, 1, 0, digitb, memo)
    cnt2 = calc(len(digita) - 1, 1, 0, digita, memo)
    if (a == 1):
        print(cnt1 - 1)
    else: print(cnt1 - cnt2)

memo = [[-1] * 200 for _ in range(20)]
digit = get_digit(10 ** 18)
calc(len(digit) - 1, 1, 0, digit, memo)
for line in sys.stdin:
    a, b = map(int, line.split())
    solve(a, b)