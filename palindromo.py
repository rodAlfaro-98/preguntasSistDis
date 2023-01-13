def isPalindrome(myString: str) -> bool:
    if len(myString) == 0:
        return True
    elif len(myString) == 1:
        return True
        
    if(myString[0] == myString[-1]):
        return isPalindrome(myString[1:len(myString)-1])
    else:
        return False

print(isPalindrome('dabale arroz ala zorra elabad'))