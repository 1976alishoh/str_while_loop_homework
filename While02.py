def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a = ""
    i = 0
    while i<len(s):
        if s[i].isalpha():
            a += s[i] 
        
        i = i + 1
    a = len(a)
    return a

print(main("python 2022"))
print(main("e324xE"))