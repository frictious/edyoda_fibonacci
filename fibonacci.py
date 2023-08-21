prevOne = 0 # Variable to keep track of the first previous value
prevTwo = 1 # Variable to keep track of the second previous value
next = 1 # Variable to show the next value
for num in range(0, 50): # Loop to move from 0 to 50
    print(next, end = " ") # Printing the next value
    next = prevOne + prevTwo # Adding the sum of the two previous values to get the next value
    prevOne = prevTwo # Assigning the second previous value to the first previous value
    prevTwo = next # Assigning the next value to be the second previous value again in order to get the next value
