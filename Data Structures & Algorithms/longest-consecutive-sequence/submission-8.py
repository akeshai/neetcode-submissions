class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        sorted_nums = sorted(set(nums))
        sequences = []
        sequence_candidates = {num:i for i,num in enumerate(sorted_nums) if num-1 not in sorted_nums}
        # print("seq Candidates: ",sequence_candidates)
        for i,candidate in enumerate(sequence_candidates):
            # print(f"Candidate: {candidate}")
            sequences.append([candidate])
            seq_index = sequence_candidates[candidate]

            for j in range(sequence_candidates[candidate],len(sorted_nums)-1):

                # print(f"comparing {sequences[j][-1]} and {sorted_nums[j+1]} ")
                # print(f"Sequences: {sequences} Current Seq Index : {seq_index}")
                if sequences[i][-1] ==sorted_nums[j+1]-1:
                    sequences[i].append(sorted_nums[j+1])

        return len(max(sequences,key=len))

