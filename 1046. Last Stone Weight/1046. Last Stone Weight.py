class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[-n for n in stones]
        heapq.heapify(heap)
        
        while len(heap)>1:
            y=-heapq.heappop(heap)
            x=-heapq.heappop(heap)
            
            if x==y:
                continue
            heapq.heappush(heap,-(y-x))

        return -heap[0] if heap else 0
        


#solution 2 using newer heapq functions


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=stones
        heapq.heapify_max(heap)
        while len(heap)>1:
            y=heapq.heappop_max(heap)
            x=heapq.heappop_max(heap)
            
            if x==y:
                continue
            else:
                y=y-x
                heapq.heappush_max(heap,y)        
        return heap[0] if heap else 0
