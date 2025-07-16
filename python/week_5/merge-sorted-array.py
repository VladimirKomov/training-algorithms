from numpy.ma.core import left_shift


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        left = m - 1
        right = n - 1
        l = m + n - 1

        while left >= 0 and right >= 0:
            if nums1[left] >= nums2[right]:
                nums1[l] = nums1[left]
                left -= 1
                print(nums1)
            else:
                nums1[l] = nums2[right]
                right -= 1
                print(nums1)
            l -= 1

        while right >= 0:
            nums1[l] = nums2[right]
            right -= 1
            l -= 1

        return nums1

if __name__ == '__main__':
    print(Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3))