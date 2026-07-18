class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left < right:
            mid = (left+right)//2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        #left == right == index that has the pivot
        pivot = left
        if target >= nums[pivot] and target <= nums[-1]:
            l = pivot
            r = len(nums) - 1
        else:
            l = 0
            r = pivot - 1

        while l <= r:
            mid = (l + r) //2 

            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return -1
            


        