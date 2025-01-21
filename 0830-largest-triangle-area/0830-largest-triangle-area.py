class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(P, Q, R):
            return 0.5 * abs(P[0] * Q[1] + Q[0] * R[1] + R[0] * P[1] - P[1] * Q[0] - Q[1] * R[0] - R[1] * P[0])
        N = len(points)
        max_area = 0
        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    max_area = max(max_area, area(points[i], points[j], points[k]))
        return max_area