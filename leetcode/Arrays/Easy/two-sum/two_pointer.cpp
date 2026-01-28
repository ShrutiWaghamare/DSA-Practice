// #include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, target;
    cin>> n;

    vector<int> arr(n);
    for(int i = 0; i < n; i++){
        cin>>arr[i];
    }

    cin>> target;

    // step 1: sort array(two pointer only work on sorted arrays)
    sort(arr.begin(), arr.end());

    // step 2; two pointers
    int left = 0;
    int right = n - 1;

    while(left < right){
        int sum = arr[left] + arr[right];
        if(sum == target){
            cout<<"Pair found"<< arr[left]<<"+ "<<arr[right]<<"="<<target<<endl;
            return 0;
        }
        else if(sum < target){
            left++;
        }
        else{
            right--;
        }
    }
    cout<<"No pair found";
    return 0;
}