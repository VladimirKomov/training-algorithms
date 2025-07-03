class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        if len(s) == 1:
            return 1

        seen = set()
        max_len = 0
        for char in s:
            if char in seen:
                if max_len < len(seen):
                    max_len = len(seen)
                seen = set()
                seen.add(char)
            else:
                seen.add(char)


        return max(max_len, len(seen))


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("dvdf"))