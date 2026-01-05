class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        sum_abs = 0
        neg = 0
        mn = float("inf")
        has_zero = False

        for row in matrix:
            for x in row:
                if x < 0:
                    neg += 1
                if x == 0:
                    has_zero = True
                ax = abs(x)
                sum_abs += ax
                mn = min(mn, ax)

        if neg % 2 == 0 or has_zero:
            return sum_abs
        return sum_abs - 2 * mn