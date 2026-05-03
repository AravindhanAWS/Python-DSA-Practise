class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowerS =  s.lower()
        vowel = "".join([char for char in lowerS if char.isalnum()])

        mid = len(vowel) // 2

        count = 0
        leng = len(vowel) - 1


        for i in range(mid):
            if vowel[i] == vowel[leng]:
                count += 1
            leng -= 1

        if vowel == " ":
            return True

        if mid == count:
            return True
        else:
            return False



        
