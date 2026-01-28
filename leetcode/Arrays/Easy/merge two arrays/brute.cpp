#include <iostream>
using namespace std;


void merge(int A[], int n, int B[], int m, int C[]){
    int i = 0, j = 0, k= 0;
    while(i < n && j < m){
        if (A[i] <= B[j]){
            C[k] = A[i];
            i++;
        }else{
            C[k] = B[j];
            j++;
        }
        k++;
    }
    while(i < n){
        C[k] = A[i];
        i++;
        k++;
    }
    while(j < m){
        C[k] = B[j];
        j++;
        k++;
    }
}
int main() {
    int A[] = {1, 3, 5, 7};
    int B[] = {2, 4, 6};

    int n = 4;
    int m = 3; 

    int C[n + m];
    merge(A, n, B, m, C);
    
    for (int i = 0; i < n + m; i++) {
        cout << C[i] << " ";
    }

    return 0;
}