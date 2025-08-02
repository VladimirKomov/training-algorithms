class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        start = 0
        ranges = []

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if i - start > 1:
                    ranges.append(str(nums[start]) + "->" + str(nums[i - 1]))
                else:
                    ranges.append(str(nums[start]))
                start = i

        if len(nums) - start > 1:
            ranges.append(str(nums[start]) + "->" + str(nums[len(nums) - 1]))
        else:
            ranges.append(str(nums[start]))

        return ranges


if __name__ == '__main__':
    solution = Solution()
    result = solution.summaryRanges([0,1,2])
    print(result)