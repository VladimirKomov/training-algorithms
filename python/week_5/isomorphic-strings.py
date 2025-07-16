class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for i in range(len(s)):
            if s[i] in s_to_t and s_to_t[s[i]] != t[i]:
                return False

            if t[i] in t_to_s and t_to_s[t[i]] != s[i]:
                return False

            s_to_t[s[i]] = t[i]
            t_to_s[t[i]] = s[i]

        return True


if __name__ == '__main__':
    print(Solution().isIsomorphic("egg","add"))