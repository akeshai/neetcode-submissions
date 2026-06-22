class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                at_i = nums[i]
                at_j = nums[j]
                if at_i+at_j == target:
                    return [i,j]