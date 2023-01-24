#This code takes in a size (n) of a staircase and creates a stair-shaped pattern of characters with that size.

#The way the code works is as follows:

#A loop is created and the variable i ranges from 1 to n+1.
#Within each loop iteration, a string is created by multiplying "#" by i.
#This string is formatted using an f-string, where it is given a minimum width of n and aligned to the right (:>{n}).
#This formatted string is printed on the screen.
#The loop ends and the code ends.
#This approach allows for the number of "#" characters to increase on each iteration of the loop, while maintaining the overall width of the output to be n, which creates the stair-shaped pattern.


def staircase(n):
    for i in range(1, n+1):
        print(f'{"#"*i:>{n}}')



        