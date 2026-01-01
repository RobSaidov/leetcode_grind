class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        list = []
        leng = len(digits)
        num = 0
        for i in range(leng):
            num += digits[i]*(10**(leng-i-1))
        
        num+=1

        leng = len(str(num))
        for i in range(leng):
            list.append((num %(10**(leng-i)) )//(10**(leng-i-1)))
        return list