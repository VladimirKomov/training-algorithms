class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        write = 0

        for read in range(len(nums)):
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1

        return write, nums


if __name__ == '__main__':
    solution = Solution().removeElement([3,2,2,3], 3)
    print(solution)