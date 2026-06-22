class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for index,val in enumerate(nums):
            hashMap[val]=index

        for index,val in enumerate(nums):
            compliment = target - val
            if (compliment in hashMap) and ( index!=hashMap[compliment]):
                return [index,hashMap[compliment] ]