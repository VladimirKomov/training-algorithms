class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p_1 = 0
        p_2 = len(s) - 1

        while p_1 < p_2:
            while p_1 < p_2 and not s[p_1].isalnum():
                p_1 += 1

            while p_2 < p_1 and not s[p_2].isalnum():
                p_2 -= 1

            if s[p_1].lower() != s[p_2].lower():
                return False

            p_1 += 1
            p_2 -= 1

        return True

if __name__ == '__main__':
    print(Solution().isPalindrome("aba"))