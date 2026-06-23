class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if not num in counter:
                counter[num] =1
            else:
                counter[num] +=1
        
        sorted_items =sorted(counter.items(),key = lambda x:x[1],reverse=True)

        return [sorted_items[i][0] for i in range(k) ]