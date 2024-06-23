class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        string = list(s)
        length = len(string)
        
        pointer1 = 0
        pointer2 = length - 1
        
        while pointer1 < pointer2:
            
            while pointer1 < pointer2 and string[pointer1] not in vowels:
                pointer1 += 1
                
            while pointer1 < pointer2 and string[pointer2] not in vowels:
                pointer2 -=1
            
            if pointer1 < pointer2:
                string[pointer1], string[pointer2] = string[pointer2], string[pointer1]
                pointer1 += 1
                pointer2 -= 1
        
        return ''.join(string)