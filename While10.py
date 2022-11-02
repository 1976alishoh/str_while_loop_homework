def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a = 0
    i = 0
    while i<len(s):
        if int(s[i])%2 == 1:
            a += int(s[i]) 
        
        i = i + 1
    
    return a
print(main("589765"))
print(main("98421"))