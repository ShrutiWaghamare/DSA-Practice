#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int arr[n];
    for(int i = 0; i < n; i++) cin >> arr[i];
    
    // Create hash array for frequency
    int hash[13] = {0};  // assuming numbers are from 0 to 12
    for(int i = 0; i < n; i++) {
        hash[arr[i]]++;
    }
    
    int number_to_count;
    cin >> number_to_count;  // the number whose count we want
    cout << hash[number_to_count] << endl;

    return 0;
}
