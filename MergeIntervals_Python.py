class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        print(intervals)


        result = []
        result.append(intervals[0])
        for i in range(1, len(intervals)):
            resultLast = result[-1]
            if resultLast[1] >= intervals[i][1]:
                continue
            elif resultLast[1] >= intervals[i][0]:
                newInterval = [resultLast[0], intervals[i][1]]
                result.pop()
                result.append(newInterval)
            else:
                result.append(intervals[i])
        return result 