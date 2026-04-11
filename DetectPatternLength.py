
def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        length = len(arr)
        count = 0

        for i in range(length - m):
            if arr[i] == arr[i + 1]:
                count += 1

                if count ==  m * (k - 1):
                    return True
            else: count == 0
        return False
