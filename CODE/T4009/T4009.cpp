#define nametask "T4009"
#include <bits/stdc++.h>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define SZ(a) (int) a.size()
#define all(a) a.begin(), a.end()
#define FOR(i, a, b) for (int i = a; i <= b; i++)
#define FOD(i, b, a) for (int i = b; i >= a; i--)

using namespace std;
typedef long long ll;
typedef pair <int, int> pi;
const int MOD = 1e9 + 7;

string L, R;
int f[10005][10][3];

void add(int &x, int y){
    x += y;
    if (x >= MOD) x -= MOD;
}

int calc(int id, bool tight, bool large_0, int pre, int flag, int sz, string &n){
    if (id >= sz) return 1;
    if ((!tight) && (f[id][pre][flag] != -1))
        return f[id][pre][flag];
    int cnt = 0;
    int maxc = (tight) ? (n[id] - '0') : 9;
    FOR(i, 0, maxc){
        int new_tight = (i == (n[id] - '0')) ? tight : 0;
        if (!large_0){
            add(cnt, calc(id + 1, new_tight, large_0 | (i > 0), i, flag, sz, n));
        }
        else{
            if (i == pre) continue;
            if (!flag){
                int new_flag = (i > pre) ? 1 : 2;
                add(cnt, calc(id + 1, new_tight, 1, i, new_flag, sz, n));
            }
            else if ((flag == 1) && (pre > i))
                add(cnt, calc(id + 1, new_tight, 1, i, 2, sz, n));
            else if (flag == 2 && (pre < i))
                add(cnt, calc(id + 1, new_tight, 1, i, 1, sz, n));
        }
    }
    if (!tight) f[id][pre][flag] = cnt;
    return cnt;
}

int solve(){
    memset(f, -1, sizeof f);
    cin >> L >> R;
    bool ck = 1;
    FOR(i, 0, SZ(L) - 2){
        if (L[i] == L[i + 1]) ck = 0;
        if (i < SZ(L) - 2){
            if (L[i] < L[i + 1] && L[i + 1] < L[i + 2]) ck = 0;
            if (L[i] > L[i + 1] && L[i + 1] > L[i + 2]) ck = 0;
        }
    }
    while (SZ(L) < SZ(R)) L = '0' + L;
    int sz = SZ(L);
    int res = (calc(0, 1, 0, 0, 0, sz, R) - calc(0, 1, 0, 0, 0, sz, L) + MOD) % MOD;
    return ((res + ck) % MOD);
}

signed main()
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    if (fopen(nametask".inp", "r")){
        freopen(nametask".inp", "r", stdin);
        freopen(nametask".out", "w", stdout);
    }
    cout << solve();    
    return 0;
}
