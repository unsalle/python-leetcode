#!/usr/bin/env python3

def romanToInt(s):
    sum = 0
    for index, char in enumerate(s):
        if char == "I":
            if index < len(s) - 1 and s[index + 1] in ["V", "X"]:
                sum -= 1 
            else: 
                sum += 1

        elif char == "V":
            sum += 5
        
        elif char == "X":
            if index < len(s) - 1 and s[index + 1] in ["L", "C"]:
                sum -= 10 
            else:
                sum += 10 
        
        elif char == "L":
            sum += 50 

        elif char == "C":
            if index < len(s) - 1 and s[index + 1] in ["D", "M"]:
                sum -= 100 
            else:
                sum += 100
        
        elif char == "D":
            sum += 500
        
        elif char == "M":
            sum += 1000
        
        print(f"Index: {index}, Character: {char}, Current sum: {sum}")

    print(f"Final sum: {sum}")
    return sum

print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))
