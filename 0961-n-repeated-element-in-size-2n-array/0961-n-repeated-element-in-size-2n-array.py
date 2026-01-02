class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        map = Counter(nums)
        n = len(nums)/2
        for k, v in map.items():
            if v == n:
                return k
        return