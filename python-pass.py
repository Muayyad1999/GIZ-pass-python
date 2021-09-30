class Solution:
    def longestPalindrome(s: str) -> str:
        temp = ''  # Temporary Storing
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if len(temp) >= j-i:
                    break
                elif s[i:j] == s[i:j][::-1]:
                    temp = s[i:j]
                    break
        return temp

Words=['babad','cbbd','ac','a',]
for k in Words:
    print(Solution.longestPalindrome(k))
