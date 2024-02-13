class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ""
        len_word1 = len(word1)
        len_word2 = len(word2)
        
        
        min_len = min(len_word1, len_word2)
        
        
        for i in range(min_len):
            result += word1[i]
            result += word2[i]
        
        
        if len_word1 > len_word2:
            result += word1[min_len:]
        elif len_word2 > len_word1:
            result += word2[min_len:]
        
        return result