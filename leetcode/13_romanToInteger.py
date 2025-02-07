#!/usr/bin/env python3


input = "LVIII"
sum = 0

for index, char in enumerate(input):
    if char == "L":
        sum += 50
    elif char == "V":
        sum += 5
    elif char == "I":
        sum += 1
    print(f"Index: {index}, Character: {char}, Current sum: {sum}")

print(f"Final sum: {sum}")
        
