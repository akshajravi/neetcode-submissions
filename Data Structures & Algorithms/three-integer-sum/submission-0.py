class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #sorted in ascending order

        result = []

        for index, value in enumerate(nums):
            #if we encounter value above 0, then we can't have 
            #a sum of zero since everything after will be positive too
            if value > 0:
                break
            
            #account for duplicates, continue to next element if duplicate
            if index > 0 and nums[index - 1] == value:
                continue
            
            left = index + 1 #element right after current index
            right = len(nums) - 1
            while left < right:
                threeSum = value + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    result.append([value,nums[left],nums[right]])
                    left +=1
                    right-=1
                    while nums[left] == nums[left-1] and left < right:
                        left+=1
        return result
