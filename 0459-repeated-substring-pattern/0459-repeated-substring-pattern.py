class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s)):
            if len(s) % i == 0:
                multiple = len(s) // i
                if s[:i]*multiple == s:
                    return True
        return False