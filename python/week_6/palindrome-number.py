class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        original = x
        reverse_n = 0

        while x > 0:
            digit = x % 10
            reverse_n = (reverse_n * 10) + digit
            x //= 10

        return original == reverse_n


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(122))