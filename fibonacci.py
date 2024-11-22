# FUnction which will begin the sequence
def fibonacciSequence(count, digit1, digit2, n):

    for x in range(int(n)):
        sum = digit1 + digit2
        print(digit1, "+", digit2, ": ", sum)
        digit1 = digit2
        digit2 = sum
        count += 1 

# File which will contain the function to begin the fibonacci sequence
def askUser():
    n = input("Please input a number to begin the fibonacci sequence: ")

    # Begin the sequence
    fibonacciSequence(1, 1, 1, n)