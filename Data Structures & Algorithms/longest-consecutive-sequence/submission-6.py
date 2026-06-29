class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        sorted_nums = sorted(set(nums))
        sequences = []
        sequence_candidates = [num for num in sorted_nums if num-1 not in sorted_nums]
        
        print("Sequence_candidates",sequence_candidates)
        for i in range(len(sequence_candidates)):
            sequences.append([sequence_candidates[i]])

            for j in range(len(sorted_nums)-1):

                # print(f"comparing {sequences[j][-1]} and {sorted_nums[j+1]} ")

                if sequences[i][-1] ==sorted_nums[j+1]-1:
                    sequences[i].append(sorted_nums[j+1])
        return len(max(sequences,key=len))

