class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        p_2 = 1

        for p_1 in range(1, len(nums)):
            if nums[p_1] != nums[p_1 - 1]:
                nums[p_2] = nums[p_1]
                p_2 += 1

        return p_2

if __name__ == '__main__':
    print(Solution().removeDuplicates([1,1,2]))