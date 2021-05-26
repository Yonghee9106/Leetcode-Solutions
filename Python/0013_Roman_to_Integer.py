##################
# First Solution #
##################

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         Roman_Dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#         num = 0
#
#         for i in range(0, len(s) - 1):                  # range from 0 to len(s)-1, because there is no s[i+1] at the end of s
#             if Roman_Dic[s[i]] < Roman_Dic[s[i+1]]:     # if right Roman is bigger than left, that is expression of 4
#                 num -= Roman_Dic[s[i]]                  # So, subtract it
#             else:                                       # if right Roman is smaller than left, that is normal
#                 num += Roman_Dic[s[i]]                  # So, just add them
#         return num + Roman_Dic[s[-1]]                   # add right last Roman because that is not in for loop range



###################
# Second Solution #
###################

class Solution:
    def romanToInt(self, s: str) -> int:
        Roman_Dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0

        s = s.replace("IV", "IIII").replace("IX", "VIIII")          # replace exceptions
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

        for char in s:                                              # and add them all
            num += Roman_Dic[char]
        return num


print(Solution().romanToInt("IV"))
