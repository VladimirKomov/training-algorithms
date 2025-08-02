class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}
        for i, n in enumerate(nums):
            if n in seen and i - seen[n] <= k:
                return True
            seen[n] = i

        return False

if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,1,2,3]
    print(s.containsNearbyDuplicate(nums, 2))