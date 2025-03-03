
import sys

sys.stdin = open("T4005.inp", "r")
sys.stdout = open("T4005.out", "w")

def get_digit(x):
    v = []
    while (x > 0):
        v.append(x % 10)
        x //= 10
    return v

def calc(id, tight, sum, k, digit, memo):
    if (id < 0):
        if (sum == k): return 1
        else: return 0
    if not tight and memo[id][sum] != -1:
        return memo[id][sum]
    cnt = 0
    c = digit[id] if tight else 9
    for i in range(c + 1):
        new_tight = tight if (i == digit[id]) else 0
        cnt += calc(id - 1, new_tight, sum + i, k, digit, memo)
    if tight == 0:
        memo[id][sum] = cnt
    return cnt

def solve(a, b, k):
    memo = [[-1] * 200 for _ in range(20)]
    digita = get_digit(a - 1)
    digitb = get_digit(b)
    cnt1 = calc(len(digitb) - 1, 1, 0, k, digitb, memo)
    cnt2 = calc(len(digita) - 1, 1, 0, k, digita, memo)
    print(cnt1 - cnt2)
    while (a < b):
        mid = (a + b) // 2
        digitmid = get_digit(mid)
        if (calc(len(digitmid) - 1, 1, 0, k, digitmid, memo) - cnt2 > 0): 
            b = mid
        else: 
            a = mid + 1
    print(a)


a, b, k = map(int, input().split())
solve(a, b, k)