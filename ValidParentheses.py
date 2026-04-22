class Solution:
    def isValid(self, s: str) -> bool:
        opening = ["(", "[", "{"]
        brackets = {"(": ")", "[": "]", "{": "}"}
        track = []

        for i in s:
            if i in opening:
                track.append(i)
            else:
                if len(track) == 0:
                    return False

                last = track[-1]

                if brackets[last] == i:
                    track.pop()
                else:
                    return False
        
        return len(track) == 0

            


        
                


