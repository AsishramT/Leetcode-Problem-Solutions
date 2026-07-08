class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        start = None
        end = None
        indexStart = None
        indexEnd = None

        for i, inter in enumerate(intervals):
            if start is None and inter[1] >= newInterval[0] and inter[0] <= newInterval[1]:
                start = inter
                indexStart = i

            if inter[1] >= newInterval[1] and end is None:
                if inter[0] <= newInterval[1]:
                    end = inter
                    indexEnd = i
                else:
                    end = newInterval
                    indexEnd = i - 1

        if start is None:
            for i, inter in enumerate(intervals):
                if newInterval[1] < inter[0]:
                    intervals.insert(i, newInterval)
                    return intervals
            intervals.append(newInterval)
            return intervals

        if end is None:
            end = intervals[-1]
            indexEnd = len(intervals) - 1
        
        fin = [
            min(start[0], newInterval[0]),
            max(end[1], newInterval[1])
        ]

        intervals = intervals[:indexStart] + intervals[indexEnd + 1:]
        intervals.insert(indexStart, fin)

        return intervals
        