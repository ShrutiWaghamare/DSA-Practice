#include <iostream>
#include <vector>
using namespace std;

vector<int> merge(vector<int>& A, vector<int>& B){
    int i = 0, j = 0;
    int n = A.size();
    int m = B.size();
    vector<int> C;

    while (i < n && j < m) {
        if (A[i] <= B[j]) {
            C.push_back(A[i]);
            i++;
        } else {
            C.push_back(B[j]);
            j++;
        }
    }

    while( i < n){
        C.push_back(A[i]);
        i++;
    }
    while (j < m) {
        C.push_back(B[j]);
        j++;
    }

    return C;


}

int main() {
    vector<int> A = {1, 3, 5, 7};
    vector<int> B = {2, 4, 6};
    vector<int> result = merge(A, B);

    for(int x: result){
        cout<< x <<" ";
    }
    return 0;
}