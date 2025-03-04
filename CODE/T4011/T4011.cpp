#define nametask "T4011"
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

int k;
string L, R;
int f[55][455][500];
bool prime[500];

void add(int &x, int y){
    x += y;
    if (x >= MOD) x -= MOD;
}

int calc(int id, bool tight, int sum, int du, int sz, string &n){
    if (id >= sz){
        return ((prime[sum]) && (du == 0));
    }
    if ((!tight) && (f[id][sum][du] != -1))
        return f[id][sum][du];
    int cnt = 0;
    int maxc = (tight) ? (n[id] - '0') : 9;
    FOR(i, 0, maxc){
        int new_tight = (i == (n[id] - '0')) ? tight : 0;
        add(cnt, calc(id + 1, new_tight, sum + i, (du * 10 + i) % k, sz, n));
    }
    if (!tight) f[id][sum][du] = cnt;
    return cnt;
}

int solve(){
    memset(prime, 1, sizeof prime);
    prime[0] = prime[1] = 0;
    for (int i = 2; i * i <= 450; i++){
        if (prime[i]) for (int j = i * i; j <= 450; j += i) prime[j] = 0;
    }
    memset(f, -1, sizeof f);
    cin >> L >> R >> k;
    int sum = 0;
    int du = 0;
    FOR(i, 0, SZ(L) - 1){
        du = (du * 10 + L[i] - '0') % k;
        sum += L[i] - '0';
    }
    while (SZ(L) < SZ(R)) L = '0' + L;
    int sz = SZ(L);
    int res = (calc(0, 1, 0, 0, sz, R) - calc(0, 1, 0, 0, sz, L) + MOD) % MOD;
    if (prime[sum] && du == 0) add(res, 1);
    return res;
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
