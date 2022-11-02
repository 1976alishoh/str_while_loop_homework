def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    a = ""
    i = 0
    while i<len(s):
        if s[i] != "a" and s[i] != "e" and s[i] != "i" and s[i] != "o" and s[i] != "u"  and s[i] != "A" and s[i] != "E" and s[i] != "I" and s[i] != "O" and s[i] != "U" :
            a += s[i] 
        
        i = i + 1
    a = len(a)
    return a
print(main("CodeschoolUz"))