def isSubset( a1, a2, n, m):
    
    set1 = set(a1)
    set2 = set(a2)
    
    if set2.issubset(set1):
        return "Yes"
    else:
        return "No"