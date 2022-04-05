class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        front, back = 0, len(s) - 1
        while(back > front):
            s[front], s[back] = s[back], s[front]
            front += 1
            back -= 1
