def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a = ""
    b = ""
    i = 0
    while i<len(s):
        if s[i].isalpha():
            a += s[i] 
        if s[i].isdigit():
            b += s[i]
        i = i + 1
    a = len(a)
    b = len(b)
    c = len(s) - a - b
    return c
print(main("#hashtag@$"))