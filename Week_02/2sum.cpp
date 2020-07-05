#include <vector>
#include <unordered_map>
using namespace std;
class Solution {

    public:
        vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> imap;
        vector<int> ans;
    
        for (int i = 0;; ++i) {
            auto it = imap.find(target - nums[i]);
        
            if (it != imap.end()) {
                ans.push_back(i);
                ans.push_back(it->second);
                return ans; 
            }
            
            imap[nums[i]] = i;
        }
    }
};