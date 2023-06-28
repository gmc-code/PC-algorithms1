import math

def add_fractions(fraction1, fraction2):
    # Unpack fractions
    numerator1, denominator1 = fraction1
    numerator2, denominator2 = fraction2
    
    # Find lowest common denominator
    lcd = denominator1 * denominator2 // math.gcd(denominator1, denominator2)
    
    # Convert each fraction to have the same denominator
    numerator1 *= lcd // denominator1
    numerator2 *= lcd // denominator2
    
    # Add numerators
    numerator_sum = numerator1 + numerator2
    
    # Simplify the fraction if possible
    gcd = math.gcd(numerator_sum, lcd)
    result = (numerator_sum // gcd, lcd // gcd)
    
    # Output sum of fractions as a mixed number if it is an improper fraction
    if result[0] > result[1]:
        whole_number = result[0] // result[1]
        remainder = result[0] % result[1]
        return f"{whole_number} {remainder}/{result[1]}"
    else:
        return f"{result[0]}/{result[1]}"

fraction1 = (1, 2)
fraction2 = (2, 3)
result = add_fractions(fraction1, fraction2)
print(f"{fraction1[0]}/{fraction1[1]} + {fraction2[0]}/{fraction2[1]} = {result}")
# 1/2 + 2/3 = 1 1/6
