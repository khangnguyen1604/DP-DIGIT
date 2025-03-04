#define nametask "T4010"
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

ll A, B;
ll f[20][1025];

vector <int> getdigit(ll x){
    vector <int> res;
    while (x > 0){
        res.pb(x % 10);
        x /= 10;
    }
    return res;
}

ll calc(int id, bool tight, bool large_0, int mask, vector <int> digit){
    if (id < 0) return 1;
    if (!tight && f[id][mask] != -1) return f[id][mask];
    int k = (tight) ? digit[id] : 9;
    ll cnt = 0;
    FOR(i, 0, k){
        bool new_tight = (i == digit[id]) ? tight : 0;
        int new_large_0 = (large_0 | (i > 0));
        if (!new_large_0) cnt += calc(id - 1, new_tight, new_large_0, 0, digit);
        else
            if (!((mask >> i) & 1)) cnt += calc(id - 1, new_tight, new_large_0, mask | (1 << i), digit);
    }
    if (tight) return cnt;
    return (f[id][mask] = cnt);
}

int solve(){
    memset(f, -1, sizeof f);
    vector <int> digitA, digitB;
    digitA = getdigit(A - 1);
    digitB = getdigit(B);
    return calc(SZ(digitB) - 1, 1, 0, 0, digitB) - calc(SZ(digitA) - 1, 1, 0, 0, digitA);
}

signed main()
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    if (fopen(nametask".inp", "r")){
        freopen(nametask".inp", "r", stdin);
        freopen(nametask".out", "w", stdout);
    }
    cin >> A >> B;
    cout << solve();    
    return 0;
}
