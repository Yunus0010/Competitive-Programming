class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
        #return: True or False
        
        #code here
        sorted_a = sorted(A)
        sorted_b = sorted(B)
        
        return sorted_a == sorted_b