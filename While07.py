def main(s):
    """
    A string of numbers is given. Find how many even numbers there are and return.
    Args:
        s: str
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
