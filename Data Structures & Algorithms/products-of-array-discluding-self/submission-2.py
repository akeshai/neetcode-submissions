class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        j = 0
        results = []
        product = 1
        while i<len(nums):
            if j == i :
                j +=1


            if j==len(nums):
                results.append(product)
                product = 1
                j = 0
                i+=1
        
            product *= nums[j]
            j+=1
       
        return results

            

            

