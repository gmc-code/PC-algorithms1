# from fractions import Fraction

# def generate_rational_sequence(denom, start, end, step):
#     sequence = []
#     for i in range(start, end, step):
#         # Create a Fraction object for each number in the sequence
#         rational_number = Fraction(i, denom)
#         mixed_fraction = rational_number.limit_denominator(1)
#         sequence.append(rational_number)
#         sequence.append(mixed_fraction)
#     return sequence

# # Generate a sequence of rational numbers from 1 to 10 with a step of 1
# sequence = generate_rational_sequence(3, 1, 11, 1)
# print("Generated sequence:", [str(num) for num in sequence])

from fractions import Fraction
fraction = Fraction(8, 3) # create a Fraction object
integer_part = fraction // 1 # get the integer part using floor division
remainder_part = fraction % 1 # get the remainder part using modulo
proper_fraction = Fraction(remainder_part) # create a proper fraction from the remainder
print(f"{integer_part} {proper_fraction}") # print the mixed number using f-string

