#include <climits>
#include <vector>
using namespace std;

class Solution {
public:
    int findMin(vector<int>& nums) {
        int l = 0;
        int r = nums.size()-1;
        int mNum = INT_MAX;

        while (l <= r){
            int mid = l+(r-l)/2;

            if (nums[r]<nums[mid]){
                l=mid+1;
            }
            else{
                r=mid-1;
            }
            mNum=min(mNum,nums[mid]);
        }
        return mNum;
        
    }
};