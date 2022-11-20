# Program Name: Check Range
# Name: Josue Cifuentes
# Date: November 12, 2022
# Purpose of a Program: to print how many times a number is in a given range

import random

def CheckRange(num): #a nubmer is passed to check its range
    #n = int(input("What is your number?"))
    if n in range(1,11): #upper bound exclusive
        print("This number is in thr range 1-10.")
        return True
    else:
        print("This number is not in the range 1-10")
        return False
    
def main():
    count  = 0 : #variable to count if the passed number is in range.
    for i in range(20):
        num = random.randint(1, 15) #upperbound inclusive
        if CheckRange(num) == True:
            count += 1
        else:
            pass
     print("The random numbers are in the given range for {} times".format(count))
 main()

'''
Not recommend
def twenty_numlist():
    print(random.randrange(1,15))
    print(random.randrange(1, 15))
    print(random.randrange(1, 15))
    print(random.randrange(1, 15))
    print(random.randrange(1, 15))
    print(random.randrange(1, 15))
    print(random.randrange(1, 15))
    print(random.randrange(1, 15))
    print(random.randrange(1, 15))
    print(random.randrange(1, 15))
    print(random.randrange(1, 15))
    print(random.randrange(1, 15))
    print(random.randrange(1, 15))
    print(random.randrange(1, 15))
    print(random.randrange(1, 15))
    print(random.randrange(1, 15))
    print(random.randrange(1, 15))
    print(random.randrange(1, 15))
    print(random.randrange(1, 15))
    print(random.randrange(1, 15))
twenty_numlist()
'''


