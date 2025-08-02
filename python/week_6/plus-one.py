class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for idx in range(len(digits) -1, -1, -1):
            val = digits[idx] + 1
            if val > 9:
                digits[idx] = 0
            else:
                digits[idx] = val
                return digits

        digits.insert(0, 1)
        return digits



if __name__ == '__main__':
    solution = Solution()
    print(solution.plusOne([9]))