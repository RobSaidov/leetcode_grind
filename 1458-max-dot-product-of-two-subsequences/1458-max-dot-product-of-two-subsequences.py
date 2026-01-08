class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        NEG_INF = -10**18

        # dp[j] will represent dp[i][j] for current i
        dp = [NEG_INF] * (m + 1)

        for i in range(n - 1, -1, -1):
            new = [NEG_INF] * (m + 1)
            for j in range(m - 1, -1, -1):
                prod = nums1[i] * nums2[j]

                # dp[j+1] is dp[i+1][j+1] (from previous row)
                take = prod + max(0, dp[j + 1])

                skip1 = dp[j]        # dp[i+1][j]
                skip2 = new[j + 1]   # dp[i][j+1] (same row)

                new[j] = max(take, skip1, skip2)
            dp = new

        return dp[0]