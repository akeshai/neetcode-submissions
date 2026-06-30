class Solution:
    def maxSubArray(self, nums):
        sub_arrays_sums = {}        
        i = 0 
        start = 0
        sub_arr_len = 1
        end = sub_arr_len
        sums = []

        while sub_arr_len<=len(nums):
            # print("Start:",sub_arr_len)
                # print(f"{start,end}")

            if (start,end-1) in sub_arrays_sums:
                # print(sub_arr_len)
                sub_arrays_sums[(start,end)] = (sub_arrays_sums[(start,end-1)]+nums[end-1])
            else:
                sub_arrays_sums[(start,end)] = sum(nums[start:end])
            # print("Sub Array: ",nums[start:end],"Sum of sub array",sum(nums[start:end]))
            # print("sub_arrays_sums :", sub_arrays_sums)
            # print()
            start +=1
            end = start + sub_arr_len
            if end >len(nums):
                start = 0
                sub_arr_len +=1
                end = start + sub_arr_len
                

        return (max( sub_arrays_sums.values()))
        
