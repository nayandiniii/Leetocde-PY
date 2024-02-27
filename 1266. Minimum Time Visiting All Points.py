class Solution:
  def distance(self, x1, y1, x2, y2):
    return max(abs(x1 - x2), abs(y1 - y2))
    
    
  def minTimeToVisitAllPoints(self, points):
    res = 0
    
    for i in range(len(points) - 1):
      (x1, y1), (x2, y2) = points[i], points[i + 1]
      res += self.distance(x1, y1, x2, y2)
    
    return res
