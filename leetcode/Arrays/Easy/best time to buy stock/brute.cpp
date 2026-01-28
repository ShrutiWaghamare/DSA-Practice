#include <bits/stdc++.h>
using namespace std;


int maxProfit(vector<int>& prices){
    int maxProfit = 0;
    int n = prices.size();
    for(int i = 0; i < n; i++){
        for(int j = i + 1; j < n; j++){
            maxProfit = max(maxProfit, prices[j]-prices[i]);
        }
    }
    return maxProfit;
}

int main() {
    vector<int> prices = {7, 1, 3, 6, 4};
    int result = maxProfit(prices);
    cout<<"Maximum Profit: "<<result<<endl;
    return 0;
}