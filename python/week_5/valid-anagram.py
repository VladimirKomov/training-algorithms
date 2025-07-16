class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        d = {}

        for c in s:
            d[c] = d.get(c, 0) + 1

        for c in t:
            if not c in d or d[c] == 0:
                return False

            d[c] -= 1

        return True

if __name__ == '__main__':
    print(Solution().isAnagram("anagram", "nagaram"))