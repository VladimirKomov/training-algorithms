class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        p_1 = 0
        p_2 = 0

        while p_1 < len(s) and p_2 < len(t):
            if s[p_1] == t[p_2]:
                p_1 += 1
            p_2 += 1

        return p_1 == len(s)



if __name__ == '__main__':
    print(Solution().isSubsequence("axc", "ahbgdc"))