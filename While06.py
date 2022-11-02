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
        if int(s[i])%2 == 0:
            a += s[i] 
        
        i = i + 1
    a = len(a)
    return a
print(main("56786543250"))
print(main("123456"))
