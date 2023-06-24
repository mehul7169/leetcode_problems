class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for i in intervals[1:]:
            last = res[-1]
            if last[1] >= i[0]:
                res.pop()
                res.append([min(last[0], last[1], i[0], i[1]), max(last[0], last[1], i[0], i[1])])
            else:
                res.append(i)
        return res