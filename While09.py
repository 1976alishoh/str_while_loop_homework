def main(s):
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a = 0
    i = 0
    while i<len(s):
        a += int(s[i]) 
        
        i = i + 1
    return a
print(main("987654"))
print(main("12"))