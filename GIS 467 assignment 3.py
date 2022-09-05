# -*- coding: utf-8 -*-
"""
1. Using a while loop, write a script that prompts the user for a number 
    and creates an ascending "wedge of stars" to the entered number.
    *
    **
    ***
    ****
2. Using a while loop, write a script that prompts the user for a number and 
    creates a descending "wedge of stars" to the entered number.
    ****
    ***
    **
    *
3. During a sale, a 10% discount is taken on purchases over $10.00.
    Write a program that accepts the purchase amount, then calculates the 
    discounted price. Ask if they want to do another calculation and repeat if 
    requested.
4. Write a program to figure out how many terms in the sum, 1 + 2 + 3 + etc., 
    are required for the sum to equal or exceed one million.
    For example: 1 +2 + 3 + 4 = 10 (4 terms equal 10)
"""

class AssignmentThree:
   
    #1 Ascending Wedge
    amount = int(input("Enter a number to create an ascending wedge of stars: "))
    start = 1
    str = ""
    while(start <= amount):
        for x in range (start):
            str = str + "*"
        print (str)
        start += 1
        str = ""
        
    #2 Descending Wedge
    amount = int(input("Enter a number to create a descending wedge of stars: "))
    start = amount
    while(start != 0):
        for x in range (start):
            str = str + "*"
        print (str)
        start -= 1
        str = ""

    #3 Do You Want the Discount
    print("\nQuinnCo is having a 10% sale on all purchases over $10!")
    answer = "yes"
    while(answer == "yes"):
        total = float(input("Please enter the amount of your purchase: $"))
        if(total >= 10):
            print(f"congratulations! You qualify for a discount! Your new price is ${round(total*.9, 2)}.")
            answer = "no"
        else:
            print(f"${total} does not qualify for a discount.")
            answer = input("Would you like to check a different amount? (yes or no)\n")
    print("Thanks, and come again!\n")
            
    #4 How Many Terms
    count = 0
    total = 0
    while(total <= 1000000):
        count += 1
        total += count
    print(f"It takes {count} terms to reach 1,000,000.")
    
    input("Press enter to exit.")