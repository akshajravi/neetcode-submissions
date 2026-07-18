class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map<int,int> check;

        for(int i = 0; i < nums.size(); i++){
            int complement = target-nums[i];

            auto it = check.find(complement);
            if(it != check.end()){
                int index = it->second;
                return {index,i};
            }
            else{
                check[nums[i]] = i;
            }
        }
    }
};
