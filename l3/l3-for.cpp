#include <iostream>
using namespace std;

// int main() {
//     int n;
//     cout<<"Enter Number: "<<endl;
//     cin>>n;
//     // cout<<"Number from 1 to n:"<<endl;
//     cout<<endl;
//     // for(int i = 1; i <= n; i += 2){
//     //     cout<<i<<endl;
//     // }
//     int sum = 0;
//     for(int i = 1; i<= n; i++){
//         if(i==5){
//             break;
//         }
//         sum += i;
//     }
//     cout<<"Sum is: "<<sum<<endl;
//     return 0;
// }

// Sum of odd numbers
// int main(){
//     int n;
//     cout<<"Enter Total number: ";
//     cin>>n;
//     cout<<endl;
//     int oddSum = 0;
//     for(int i = 1; i<=n; i++){
//         if(i % 2 != 0){
//             oddSum += i;
//         }
//     }
//     cout<<"OddSum is: "<<oddSum<<endl;
//     return 0;
// }

// DO while loop - executes atleast once even if condition is false

int main(){
    int n;
    cout<<"Enter Total number: ";
    cin>>n;
    cout<<endl;
    int i = 1;
    do{
        cout<<i<<" ";
        i++;
    }while(i >= n);
    cout<<endl;
    return 0;

}