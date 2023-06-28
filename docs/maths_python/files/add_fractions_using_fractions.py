from fractions import Fraction

fraction1 = Fraction(1, 3)
fraction2 = Fraction(2, 3)
result = fraction1 + fraction2
whole_number = int(result)
if whole_number > 0:
    fraction = result - whole_number
    if fraction > 0:
        print(f"{fraction1} + {fraction2} = {whole_number} {fraction}")
        # 1/2 + 2/3 = 1 1/6
    else:
        print(f"{fraction1} + {fraction2} = {result}")
        # 1/3 + 2/3 = 1
else:
    print(f"{fraction1} + {fraction2} = {result}")
    # 1/6 + 2/3 = 5/6