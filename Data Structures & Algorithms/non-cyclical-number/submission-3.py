class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            total = 0
            number = n
            while number > 0:
                total += (number % 10) ** 2
                number //= 10
            if total == 1:
                return True
            if total in seen:
                return False
            seen.add(total)
            n = total

                