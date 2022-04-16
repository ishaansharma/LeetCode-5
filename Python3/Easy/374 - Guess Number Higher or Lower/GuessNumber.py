class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        first, last = 1, n

        while first <= last:
            middle = (first + last) // 2
            
            if guess(middle) == 0:
                return middle
            if guess(middle) == 1:
                first = middle + 1
            elif guess(middle) == -1:
                last = middle - 1
                
