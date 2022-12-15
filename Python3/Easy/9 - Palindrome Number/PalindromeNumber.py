class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return str(x) == str(x)[::-1]
        if x < 0:
            return False
        copy, reverse = x, 0

        while copy:
            reverse *= 10
            reverse += copy % 10
            copy //= 10

        return x == reverse
