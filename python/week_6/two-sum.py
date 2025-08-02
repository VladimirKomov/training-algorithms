class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for index, num in enumerate(nums):
            goal = target - num
            if goal in seen:
                return [seen[goal], index]
            seen[num] = index




if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = s.twoSum(nums, target)
    print(result)