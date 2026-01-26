#include <iostream>
#include<vector>
using namespace std;


class Solution{
public:
    void moveZeros(vector<int>& nums){
        int k = 0;
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] != 0){
                nums[k] = nums[i];
                k++;
            }
        }
        for(int i = k; i < nums.size(); i++){
            nums[i] = 0;
        }
    }
};

int main() {
    Solution m;;
    vector<int> nums = {0, 1, 0, 3, 12};
    m.moveZeros(nums);
    for(int i = 0; i < nums.size(); i++){
        cout<<nums[i]<<endl;
    }
    return 0;
}