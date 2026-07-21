import random

print("Enter is my magic number (1 to 100) ?")
mynumber = random.randint(1,100)
ntries = 1
yourguess = -1
while ntries < 7 and  ______________:
    msg = str(ntries) + ">>"
    if (ntries == 6) :
        _________________________
    yourguess = int(input(msg))
    if ______________________:
        print("--> too high")
    _________________________
        print("--> too low")
    ntries += 1

if ________________________:
    print("Yes! it's" , mynumber)
else :
    print("Sorry! my number is", mynumber)