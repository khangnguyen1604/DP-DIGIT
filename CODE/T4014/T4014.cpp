#define nametask "T4014"
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

ll f[20][172];
ll res[22], A[22], B[22];

vector <int> getdigit(ll x){
    vector <int> res;
    while (x > 0){
        res.pb(x % 10);
        x /= 10;
    }
    return res;
}

ll calc(int id, bool tight, int sum, int d, vector <int> digit){
    if (id < 0) return (sum == d);
    if (!tight && f[id][sum] != -1) return f[id][sum];
    int k = (tight) ? digit[id] : 9;
    ll cnt = 0;
    FOR(i, 0, k){
        bool new_tight = (i == digit[id]) ? tight : 0;
        cnt += calc(id - 1, new_tight, sum + i, d, digit);
    }
    if (tight) return cnt;
    return (f[id][sum] = cnt);
}

ll solve(ll a, ll b, int d){
    vector <int> digitA, digitB;
    digitA = getdigit(a - 1);
    digitB = getdigit(b);
    return calc(SZ(digitB) - 1, 1, 0, d, digitB) - calc(SZ(digitA) - 1, 1, 0, d, digitA);
}

signed main()
{   
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    if (fopen(nametask".inp", "r")){
        freopen(nametask".inp", "r", stdin);
        freopen(nametask".out", "w", stdout);
    }
    int t;
    cin >> t;
    FOR(i, 1, t){
        cin >> A[i] >> B[i];
    }
    vector <int> digitM = getdigit((ll)1e19);
    FOR(i, 1, 9 * 19){
        memset(f, -1, sizeof f);
        calc(SZ(digitM) - 1, 1, 0, i, digitM);
        FOR(j, 1, t) res[j] += solve((A[j] + i - 1) / i, B[j] / i, i);
    }
    FOR(i, 1, t) cout << res[i] << '\n';
    return 0;
}
