class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == [] :
            return 0
        nums  = sorted(set(nums))
        start_candidates = []
        sequences = []
        for i in range(len(nums)):
            if nums[i]-1 not in nums:
                start_candidates.append(nums[i])
        # print("Candidates: ",start_candidates)

        for candidate in start_candidates:
            # print("For candidate :", candidate)
            sequence = []
            sequence.append(candidate)
            i = 1
            while candidate+i in nums :
                sequence.append(candidate+i)
                i+=1
                # print("Sequences",sequence)
            sequences.append(sequence)
        # print("Sequences",sequences)
        return len(max(sequences,key=len))
