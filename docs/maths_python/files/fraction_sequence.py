from fractions import Fraction

def generate_rational_sequence(denom, start, end, step):
    sequence = []
    for i in range(start, end, step):
        # Create a Fraction object for each number in the sequence
        rational_number = Fraction(i, denom)
        mixed_fraction = rational_number.limit_denominator(1)
        sequence.append(rational_number)
        sequence.append(mixed_fraction)
    return sequence

# Generate a sequence of rational numbers from 1 to 10 with a step of 1
sequence = generate_rational_sequence(3, 1, 11, 1)
print("Generated sequence:", [str(num) for num in sequence])


