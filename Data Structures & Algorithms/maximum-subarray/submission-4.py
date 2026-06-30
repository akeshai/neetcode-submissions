import numpy as np

class Solution:
    def maxSubArray(self, nums):
        sub_arrays_sums = {}        
        start = 0
        sub_arr_len = 1
        end = sub_arr_len
        max_sum = -np.inf
        _sum = None
        while sub_arr_len<=len(nums):
            # print("Start:",sub_arr_len)
                # print(f"{start,end}")
            if (start,end-1) in sub_arrays_sums:
                # print(sub_arr_len)
                _sum = sub_arrays_sums[(start,end-1)]+nums[end-1]
                sub_arrays_sums[(start,end)] = _sum
            else:
                _sum = sum(nums[start:end])
                sub_arrays_sums[(start,end)] = _sum

            if _sum>max_sum:
                max_sum = _sum
            # print("Sub Array: ",nums[start:end],"Sum of sub array",sum(nums[start:end]))
            # print("sub_arrays_sums :", sub_arrays_sums)
            # print()
            start +=1
            end = start + sub_arr_len
            if end >len(nums):
                start = 0
                sub_arr_len +=1
                end = start + sub_arr_len
                

        return max_sum
        
