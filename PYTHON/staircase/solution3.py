#This code takes in a size (n) of a staircase and creates a stair-shaped pattern of characters with that size. For example, if n is set to 4, it will print the following on the screen:
#The way the code works is as follows:

#A loop is created and the variable i ranges from 1 to n+1.
#Within each loop iteration, (n-i) spaces and i # characters are printed.
#These spaces and # characters are combined and printed on the screen.
#The loop ends and the code ends.

def staircase(n):
    # Write your code here
    for i in range(1,n+1):
        print(" "*(n-i)+"#"*i)