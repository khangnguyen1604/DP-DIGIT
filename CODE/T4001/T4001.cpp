#define nametask "T4001"
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
bool prime[200];

bool check_nt(int n){
    if (n < 2) return 0;
    for (int i = 2; i * i <= n; i++){
        if (n % i == 0) return 0;
    }
    return 1;
}

vector <int> getdigit(ll x){
    vector <int> res;
    while (x > 0){
        res.pb(x % 10);
        x /= 10;
    }
    return res;
}

ll calc(int id, bool tight, int sumdigit, vector <int> digit){
    if (id < 0) return (prime[sumdigit]);
    if (!tight && f[id][sumdigit] != -1) return f[id][sumdigit];
    int k = (tight) ? digit[id] : 9;
    ll cnt = 0;
    FOR(i, 0, k){
        bool new_tight = (i == digit[id]) ? tight : 0;
        cnt += calc(id - 1, new_tight, sumdigit + i, digit);
    }
    if (tight) return cnt;
    return (f[id][sumdigit] = cnt);
}

void solve(){
    memset(f, -1, sizeof f);
    FOR(i, 1, 9 * 18) prime[i] = check_nt(i);
    vector <int> digitA, digitB;
    digitA = getdigit(A - 1);
    digitB = getdigit(B);
    cout << calc(SZ(digitB) - 1, 1, 0, digitB) - calc(SZ(digitA) - 1, 1, 0, digitA);
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
