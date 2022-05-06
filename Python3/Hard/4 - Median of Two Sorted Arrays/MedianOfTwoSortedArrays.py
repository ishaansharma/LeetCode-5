class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sumLen = len(nums1) + len(nums2)
        half = sumLen // 2
        a, b = nums1, nums2
        
        if len(b) < len(a):
            a, b = b, a
        
        l, r = 0, len(a) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2
            
            aLeft = a[i] if i >= 0 else float("-inf")
            aRight = a[i + 1] if i < len(a) - 1 else float("inf")
            bLeft = b[j] if j >= 0 else float("-inf")
            bRight = b[j + 1] if j < len(b) - 1 else float("inf")
            
            if aLeft <= bRight and bLeft <= aRight:
                if sumLen % 2:
                    return min(aRight, bRight)
                return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
            elif aLeft > bRight:
                r = i - 1
            else:
                l = i + 1
                
