#include <iostream>
using namespace std;

// **Problem 1:** Sum of all numbers from 1 to n divisible by 3
// int main() {
//     int num;
//     int sum = 0;
//     cout<<"Enter Number: ";
//     cin>>num;
//     cout<<endl;
//     for(int i = 1; i <= num; i++){
//         if(i % 3 == 0){
//             sum += i;
//         }
//     }
//     cout<<"Sum of all numbers from 1 to n divisible by 3: "<<sum<<endl;
//     return 0;
// }

// Factorial

int main(){
    int n;
    cout<<"Enter number: ";
    cin>>n;
    cout<<endl;
    int fact = 1;
    for(int i = 1; i <= n; i++){
        fact = fact * i;
    }
    cout<<"Factorial of "<<n<<" is "<<fact<<endl;
    return 0;

}