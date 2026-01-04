class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        sum1 = 0
        count = 0
        for num in nums:
            sum2 = 0
            for i in range(1, num+1):
                if num%i==0:
                    count +=1
                    sum2+=i
            if count ==4:
                sum1+=sum2
            count = 0
        return sum1
