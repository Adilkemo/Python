# Programming for Everybody (Getting Started with Python)
# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

largest = 0
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break
    try:
        num1=int(num)
        if(num1>largest):
            largest=num1
        elif smallest is None or num1<smallest:
             smallest = num1
    except:
        print('Invalid input')
        continue


print("Maximum is", largest)
print("Minimum is",smallest)
