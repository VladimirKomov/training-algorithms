class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)
            n = sum(int(d) ** 2 for d in str(n))

        return True



if __name__ == '__main__':
    s = Solution()
    print(s.isHappy(19))


