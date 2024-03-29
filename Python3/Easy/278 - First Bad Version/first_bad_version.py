# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        first, last = 1, n
        while first <= last:
            middle = (first + last) // 2
            if isBadVersion(middle) is True and isBadVersion(middle - 1) is False:
                return middle
            if isBadVersion(middle) is False:
                first = middle + 1
            else:
                last = middle - 1
