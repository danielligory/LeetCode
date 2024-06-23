class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        list_t = list(t)
        list_s = list(s)
        while (len(list_t) != 0):
            if list_t[0] not in list_s:
                return list_t[0]
            else:
                list_s.remove(list_t[0])
                list_t.remove(list_t[0])
        
        return list_t[0]
                
                
            