class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = map(str,digits)
        s = ''.join(s)
        s = int(s)
        onePlus = s + 1

        onePlusStr = str(onePlus)

        return [int(char) for char in onePlusStr]



        
        


        
