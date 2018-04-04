"""
Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

For example, Given s = “eceba”,

T is "ece" which its length is 3.
"""


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """

        mydict = {}
        for c in s:
            mydict[c] = 0

        start, end = 0, 0
        letters = []
        maxlen = 0

        while end < len(s):

            mydict[s[end]] += 1
            if mydict[s[end]] == 1:
                letters.append(s[end])

            while len(letters) > 2 and start < end:
                start += 1
                mydict[s[start - 1]] -= 1
                if mydict[s[start - 1]] == 0:
                    letters.remove(s[start - 1])

            if end - start + 1 > maxlen:
                maxlen = end - start + 1

            end += 1

        return maxlen



