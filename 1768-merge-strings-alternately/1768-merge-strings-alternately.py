class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = []
        word1_list = list(word1)
        word2_list = list(word2)
        length1 = len(word1_list)
        length2 = len(word2_list)
        
        for i in range(min(length1, length2)):
            answer.append(word1_list[i])
            answer.append(word2_list[i])
        
        if length1 < length2:
            answer.extend(word2_list[length1:])
        else:
            answer.extend(word1_list[length2:])
        
        return ''.join(answer)