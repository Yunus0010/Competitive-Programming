class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        union_array = a[:n] + b[:m]
        union_set = set(union_array)
        return len(union_set)