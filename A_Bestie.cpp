#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define N 1000006
#define SetBit(x, k) (x |= (1LL << k))
#define ClearBit(x, k) (x &= ~(1LL << k))
#define CheckBit(x, k) ((x>>k)&1)
#define M 10000000007
#define all(x) x.begin(), x.end()
#define kill(x) cout << x << endl;


int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while(t--){
        int n;
        cin >> n;
        int g = 0;
        for(int i = 0; i < n; i++){
            int x;
            cin >> x;
            g = gcd(x, g);

        }
        if(g == 1) cout << 0 << endl;
        else if(gcd(n, g) == 1)cout << 1 << endl;
        else if(gcd(n-1,g)==1)cout << 2 << endl;
        else cout << 3 << endl;
    }

    return 0;
}