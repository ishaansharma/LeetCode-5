class Solution(object):
    def plusOne(self, digits):
        digits = "".join([str(i) for i in digits])
        num = int(digits)
        num += 1
        return list(str(num))
