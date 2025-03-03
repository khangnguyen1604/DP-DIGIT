#define nametask "T4007"
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
ll f[20][200];

vector <int> getdigit(ll x){
    vector <int> res;
    while (x > 0){
        res.pb(x % 10);
        x /= 10;
    }
    return res;
}

ll calc(int id, bool tight, int sum, vector <int> digit){
    if (id < 0) {
        return (sum == 101);
    }
    if (!tight && f[id][sum] != -1) return f[id][sum];
    int k = (tight) ? digit[id] : 9;
    ll cnt = 0;
    FOR(i, 0, k){
        bool new_tight = (i == digit[id]) ? tight : 0;
        int new_sum = sum + ((id % 2 == 0) ? -i : i);
        cnt += calc(id - 1, new_tight, new_sum, digit);
    }
    if (tight) return cnt;
    return (f[id][sum] = cnt);
}

void solve(){
    memset(f, -1, sizeof f);
    vector <int> digitA, digitB;
    digitA = getdigit(A - 1);
    digitB = getdigit(B);
    cout << calc(SZ(digitB) - 1, 1, 100, digitB) - calc(SZ(digitA) - 1, 1, 100, digitA);
}

signed main()
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    if (fopen(nametask".inp", "r")){
        freopen(nametask".inp", "r", stdin);
        freopen(nametask".out", "w", stdout);
    }
    cin >> A >> B;
    solve();
    return 0;
}
