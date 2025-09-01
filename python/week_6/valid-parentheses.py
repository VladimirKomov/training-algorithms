class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses = {'(' : ')',  '{' : '}', '[' : ']'}
        #parentheses = {')' : '(',  '}' : '{', ']' : '['}
        if len(s) == 0:
            return False

        if len(s) % 2 != 0:
            return False

        steck = []

        for s in s:
            if s in parentheses:
                steck.append(s)
            else:
                last = steck.pop()
                if parentheses[last] != s:
                    return False

        return steck == []




if __name__ == '__main__':
    s = Solution()
    print(s.isValid("([)]"))