class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = list(s)
        list_t = list(t)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if list_s[0] in list_t:
                list_t.remove(list_s[0])
                list_s.remove(list_s[0])
        
        return list_t == [] and list_s == []
            
        
        