class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heapq = [-stone for stone in stones]
        heapq.heapify(max_heapq)
        while len(max_heapq) > 1 :
            stones1 = -heapq.heappop(max_heapq)
            stones2 = -heapq.heappop(max_heapq)
            if stones1 != stones2 :
                heapq.heappush(max_heapq , -(stones1 - stones2))
        
        max_heapq.append(0)
        return abs(max_heapq[0])
