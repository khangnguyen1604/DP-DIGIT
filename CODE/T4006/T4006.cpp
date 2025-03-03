#define nametask "T4006"
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

string n;
int f[1005][3];

void add(int &x, int y){
    x += y;
    if (x >= MOD) x -= MOD;
}

int calc(int id, bool tight, int rem, int sz){
    if (id >= sz)
        return ((rem == 0) && (tight == 0));
    if ((!tight) && (f[id][rem] != -1)) return f[id][rem];
    int cnt = 0;
    int maxc = (tight) ? (n[id] - '0') : 9;
    FOR(i, 0, maxc){
        int new_tight = (i == (n[id] - '0')) ? tight : 0;
        add(cnt, calc(id + 1, new_tight, (rem + i * i) % 3, sz));
    }
    if (!tight)
        f[id][rem] = cnt;
    return cnt;
}

void solve(){
    memset(f, -1, sizeof f);
    cin >> n;
    int sz = SZ(n);
    cout << calc(0, 1, 0, sz);
}

signed main()
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    if (fopen(nametask".inp", "r")){
        freopen(nametask".inp", "r", stdin);
        freopen(nametask".out", "w", stdout);
    }
    solve();
    return 0;
}
