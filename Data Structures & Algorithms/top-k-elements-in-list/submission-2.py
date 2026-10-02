class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)              # 1. frequency of each number
        return heapq.nlargest(k, count.keys(), key=count.get)  # 2. pick top k