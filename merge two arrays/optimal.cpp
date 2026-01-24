#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = m - 1;       // Last element of nums1's valid part
        int j = n - 1;       // Last element of nums2
        int k = m + n - 1;   // Last position of nums1 (total size)

        // Merge from the back
        while(i >= 0 && j >= 0) {
            if(nums1[i] > nums2[j]) {
                nums1[k] = nums1[i];
                i--;
            } else {
                nums1[k] = nums2[j];
                j--;
            }
            k--;
        }

        // Copy any remaining elements from nums2
        while(j >= 0) {
            nums1[k] = nums2[j];
            j--;
            k--;
        }
    }
};

int main() {
    Solution sol;

    vector<int> nums1 = {1, 3, 5, 0, 0, 0};
    vector<int> nums2 = {2, 4, 6};
    int m = 3, n = 3;

    sol.merge(nums1, m, nums2, n);

    cout << "Merged array: ";
    for(int num : nums1) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
