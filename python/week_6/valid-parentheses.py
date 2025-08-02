class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses = {'(' : ')',  '{' : '}', '[' : ']'}
        if len(s) == 0:
            return False

        if len(s) % 2 != 0:
            return False

        

        for i in range(int(len(s) / 2)):
            if s[len(s) - 1 - i] != parentheses[s[i]] or s[i + 1] != parentheses[s[i]]:
                return False

        return True




if __name__ == '__main__':
    s = Solution()
    print(s.isValid("()[]{}"))