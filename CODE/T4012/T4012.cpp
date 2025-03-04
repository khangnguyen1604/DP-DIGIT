#define nametask "T4012"
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

ll A, B;
ll f[20][165];

vector <int> getdigit(ll x){
    vector <int> res;
    while (x > 0){
        res.pb(x % 10);
        x /= 10;
    }
    return res;
}

void add(int &x, int y){
    x += y;
    if (x >= MOD) x -= MOD;
}

int calc(int id, bool tight, int sum, vector <int> digit){
    if (id < 0) return sum;
    if (!tight && f[id][sum] != -1) return f[id][sum];
    int k = (tight) ? digit[id] : 9;
    int cnt = 0;
    FOR(i, 0, k){
        bool new_tight = (i == digit[id]) ? tight : 0;
        add(cnt, calc(id - 1, new_tight, sum + i, digit));
    }
    if (tight) return cnt;
    return (f[id][sum] = cnt);
}

int solve(){
    memset(f, -1, sizeof f);
    vector <int> digitA, digitB;
    digitA = getdigit(A - 1);
    digitB = getdigit(B);
    return (calc(SZ(digitB) - 1, 1, 0, digitB) - calc(SZ(digitA) - 1, 1, 0, digitA) + MOD) % MOD;
}

signed main()
{
    if (fopen(nametask".inp", "r")){
        freopen(nametask".inp", "r", stdin);
        freopen(nametask".out", "w", stdout);
    }
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    cin >> A >> B;
    cout << solve();
    return 0;
}
