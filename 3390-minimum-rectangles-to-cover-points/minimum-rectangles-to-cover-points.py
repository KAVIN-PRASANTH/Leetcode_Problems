class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points.sort(key =lambda e:e[0])
        j = 0
        cnt = 0
        for i in range(len(points)):
            if points[i][0] - points[j][0] <= w:
                continue
            else:
                cnt += 1
                j = i
        return cnt+1
        