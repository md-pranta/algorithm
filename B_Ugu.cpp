#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define N 1000006
#define SetBit(x, k) (x |= (1LL << k))
#define ClearBit(x, k) (x &= ~(1LL << k))
#define CheckBit(x, k) ((x>>k)&1)
#define M 10000000007
#define all(x) x.begin(), x.end()
#define kill(x) return cout << x << endl, void();


int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;
    while (t--){
        int n;
        cin >> n;

        string s;
        cin >> s;
        int flag = 0;
        int oparation = 0;
        for (int i = 0; i < n-1;i++){
            if (flag && (s[i] == '0' && s[i+1]=='1')){
                oparation++;
                flag = 0;
            }
            else if(s[i] == '1' && s[i+1]=='0'){
                oparation++;
                flag = 1;
            }
        }
        cout << oparation << endl;
    }

    return 0;
}