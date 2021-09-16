def isPallindrome(num):
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    if(temp==rev):
        print("The number is palindrome!")
        return True
    else:
        print("Not a palindrome!")
        return False