"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = sorted([float(value) for value in input().split(",")])
        
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numlength = len(numbers)
if numlength%2 != 0:
    print(numbers[int((numlength)//2)])
else:
    print( (( numbers[int(numlength/2)-1] ) + numbers[int(numlength/2)]) / 2)