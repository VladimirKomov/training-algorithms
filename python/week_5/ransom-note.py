from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        meg_dict = Counter(magazine)

        for l in ransomNote:
            if meg_dict.get(l, -1) <= 0:
                return False
            meg_dict[l] = meg_dict.get(l, -1) - 1

        return True


if __name__ == '__main__':
    print(Solution().canConstruct("aa", "ab"))