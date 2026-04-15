class Solution:
    def greatestLetter(self, s: str) -> str:
        seen = set()
        pairs = []
        max_char = ""
        for i in s:
            if i not in seen:
                seen.add(i)
            
        for j in seen:
            if j.lower() in seen:
                if j == j.upper():
                    pairs.append(j)
        for k in pairs:
            cand = k
            max_char = max(max_char,cand)


        return max_char
