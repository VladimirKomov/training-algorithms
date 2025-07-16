class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        p_to_s = {}
        s_to_p = {}

        lst_s = s.split(" ")

        for i in range(len(pattern)):
            if pattern[i] in p_to_s and p_to_s[pattern[i]] != lst_s[i]:
                return False

            p_to_s[pattern[i]] = lst_s[i]
            s_to_p[lst_s[i]] = pattern[i]

        return True


if __name__ == '__main__':
    print(Solution().wordPattern("abba","dog cat cat dog"))