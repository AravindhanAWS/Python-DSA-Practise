import math

class Solution:
    def countTriples(self, n: int) -> int:
        counter = 0
        
        for i in range(1,n+1):
            for j in range(1,n+1):
                k  = math.sqrt(i * i + j * j)
                
                if k == int(k) and k <= n:
                    counter += 1
        return counter


        
