import math

numOfSailor = input('Enter the number of sailors on the island: ')

try:
    numOfSailor = int(numOfSailor)
    while(numOfSailor <2):
        numOfSailor = int(input('There must be 2 or more sailors on the island try again: '))
except ValueError:
    print ("Could not convert given number to an integer.")

coconuts = int(math.pow(numOfSailor, numOfSailor) - (numOfSailor-1))

print("There is a total of %i coconuts on the island."% (coconuts))