class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        can = None

        for n in nums:
            if count == 0:
                can = n
            if n == can:
                count += 1
            else:
                count -= 1

        return can


if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement([2,1,2,1,2,1,2]))