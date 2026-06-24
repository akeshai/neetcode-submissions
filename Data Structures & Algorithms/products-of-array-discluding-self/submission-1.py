class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        j = 0
        results = []
        product = 1
        element_remaining = len(nums)-1
        while i<len(nums):
            if i ==j :
                j+=1
            product= product* nums[j]
            element_remaining-=1
            j+=1
            if element_remaining==0:

                i+=1
                j=0
                results.append(product)
                product = 1
                element_remaining = len(nums)-1
            
        
        return results

            

            

