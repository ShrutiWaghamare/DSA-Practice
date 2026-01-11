#include <iostream>
using namespace std;

// int main() {
//     int num = 4;
//     if (num>2){
//         cout<<"Greater than 2"<<endl;
//     }
//     return 0;
// }

// int main() {
//     int num;
//     cout<<"Enter the number: "<<endl;
//     cin>>num;
//     // if (num % 2 == 0){
//     //     cout << "Number is mulptiple of 2" << endl;
//     // }else{
//     //     cout<<"Not a multiple of 2"<<endl;
//     // }
//     // return 0;
//     if (num >= 0){
//         cout<<"Number is positive"<<endl;
//     }else
//         cout<<"Negative"<<endl;
//     return 0;
// }

int main(){
    char ch;
    cout<<"Enter Character: "<<endl;
    cin>>ch;
    // if(ch >= 'a' && ch <= 'z'){
    //     cout<<"Lower case!"<<endl;
    // }
    // else{
    //     cout<<"Upper case!"<<endl;
    // }
    if (ch >= 65 && ch <= 90){
        cout<<"Upper case!"<<endl;
    }
    else{
        cout<<"Lower case!"<<endl;
    }
    return 0;
}
