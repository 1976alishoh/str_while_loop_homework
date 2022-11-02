def main(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a = ""
    i = 0
    while i<len(s):
        if s[i].isupper():
            a += s[i] 
        
        i = i + 1
    a = len(a)
    return a
print(main("CodeschoolUz"))