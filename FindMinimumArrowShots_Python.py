class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        print(points)
        l = r = points[0][1]
        output = 0

        for p in points[1:]:
            if l < p[0]:  
                output += 1
                l = p[1]
            else:
                l = min(l, p[1])
        return output + 1