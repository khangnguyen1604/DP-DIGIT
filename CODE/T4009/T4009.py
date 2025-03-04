import sys

sys.stdin = open("T4009.inp", "r")
sys.stdout = open("T4009.out", "w")

MOD = int(1e9 + 7)

def add(x, y):
    return (x + y) % MOD

def calc(id, tight, large_0, pre, flag, sz, n, dp):
    if id >= sz:
        return 1
    if not tight and dp[id][pre][flag] != -1:
        return dp[id][pre][flag]
    
    cnt = 0
    maxc = int(n[id]) if tight else 9
    
    for i in range(maxc + 1):
        new_tight = tight and (i == int(n[id]))
        if not large_0:
            cnt = add(cnt, calc(id + 1, new_tight, large_0 or (i > 0), i, flag, sz, n, dp))
        else:
            if i == pre:
                continue
            if flag == 0:
                new_flag = 1 if i > pre else 2
                cnt = add(cnt, calc(id + 1, new_tight, True, i, new_flag, sz, n, dp))
            elif flag == 1 and pre > i:
                cnt = add(cnt, calc(id + 1, new_tight, True, i, 2, sz, n, dp))
            elif flag == 2 and pre < i:
                cnt = add(cnt, calc(id + 1, new_tight, True, i, 1, sz, n, dp))
    
    if not tight:
        dp[id][pre][flag] = cnt
    return cnt

def solve():
    L, R = input().split()
    
    ck = True
    for i in range(len(L) - 1):
        if L[i] == L[i + 1]:
            ck = False
        if i < len(L) - 2:
            if L[i] < L[i + 1] and L[i + 1] < L[i + 2]:
                ck = False
            if L[i] > L[i + 1] and L[i + 1] > L[i + 2]:
                ck = False
    
    while len(L) < len(R):
        L = '0' + L
    
    sz = len(L)
    dp = [[[-1] * 3 for _ in range(10)] for _ in range(sz)]
    
    res = (calc(0, True, False, 0, 0, sz, R, dp) - calc(0, True, False, 0, 0, sz, L, dp) + MOD) % MOD
    
    return (res + ck) % MOD

print(solve())
