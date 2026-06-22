class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=0
        while (i<=len(nums)-1):
                j+=1

                at_i = nums[i]
                at_j = nums[j]

                if at_i+at_j == target:
                    return [i,j]
                    
                if j>=len(nums)-1:
                    i+=1
                    j=i
                
