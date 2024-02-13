def freqAlphabets(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    i = len(s) - 1
    
    while i >= 0:
        if s[i] == '#':
            num = int(s[i-2:i])
            i -= 3
        else:
            num = int(s[i])
            i -= 1
        result = alphabet[num - 1] + result
    
    return result

# Test
s = "10#11#12"
print(freqAlphabets(s))  # Output: "jkab"
