#include <iostream>
using namespace std;


int binTodec(int binNum){
    int ans = 0, pow = 1;

    while(binNum > 0){
        int lastDigit = binNum % 10;
        binNum = binNum / 10;

        ans = ans + (lastDigit * pow);
        pow = pow * 2;
    }
    return ans;
}
int main() {
    int binaryNumber = 110;
    cout<<binTodec(binaryNumber)<<endl;
    return 0;
}