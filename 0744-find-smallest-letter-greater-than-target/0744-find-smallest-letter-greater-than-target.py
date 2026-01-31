class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        res = letters[0]
        flag = False


        for char in letters:
            if not flag:
                if char > target:
                    res = char
                    flag = not flag
            else:
                if char> target and char < res:
                    res = char
            
        return res