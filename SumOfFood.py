# Program Name: Sum of food
# Name: Josue Cifuentes
# Date: November 12, 2022
# Purpose of a Program: sums the price of each food item in a dictionary
import math

def SumOfFood(d): #pass the dictionary
    #foodDict = (3.50,5.30,9.45,5.75)
    #print(sum(foodDict))
    return sum(d.values())   #values function return a list of prices

def main():
    foodDict = (3.50,5.30,9.45,5.75)
    print("Total amount is ${}".format(SumOfFood(foodDict))
          
main()
