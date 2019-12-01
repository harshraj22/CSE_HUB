using namespace std;

#define ll long long int

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    int test;
    cin >> test;
    while(test--){
        ll n,k,i;
        cin >> n >> k;
        vector<int> v(k),org(n+1);
        iota(org.begin(), org.end(), 0);
        for(int i=0;i<k;i++){
            cin >> v[i];
            org[v[i]] = -1;
        }
        if((k==1 && n>1) || (k==2 && v.back()-1 != v[0])){
            cout << "NO\n";
            continue;
        }
        deque<ll> pre,post;
        for(i=1;i<=n;i++){
            if(org[i] != -1)
                break;
        }        
        int min_ind = i;
        // cout << "min ind is " << min_ind << '\n';
        for(auto it:v){
            pre.push_back(it);
            if(it == v.back())
                break;
            else if(it == v[0])
                continue;
            for(int i=it-1;i>=min_ind;i--){
                if(org[i] != -1){
                    org[i] = -1;
                    pre.push_back(i);
                }
            }
            min_ind = it;
        }
        for(int i=v.front();i>0;i--){
            if(org[i] != -1){
                pre.push_back(i);
                org[i] = -1;
            }
        }
        for(int i=min_ind;i<=n;i++){
            if(org[i] != -1){
                pre.push_front(i);
                // pre.insert(0,);
                org[i] = -1;
            }
        }
        cout << "YES\n";
        for(auto it:pre)
            cout << it << ' ';
        cout << '\n';


    }

    return 0;
}
