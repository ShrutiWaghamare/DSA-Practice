def leapYear(n):
    if n % 400 == 0:
        return True
    elif n % 100 == 0:
        return False
    elif n % 4 == 0:
        return True
    else:
        return False
        
year = int(input("Enter year: "))
if leapYear(year):
    print("It is Leap Year")
else:
    print("Not a Leap Year")
        
    