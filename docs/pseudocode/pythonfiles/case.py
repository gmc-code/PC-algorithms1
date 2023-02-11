point = (2, 3)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"{y} on Y axis")
    case (x, 0):
        print(f"{x} on X axis")
    case (x, y):
        print(f"{x} on X axis, {y} on Y axis")
    case _:
        print("Invalid point")