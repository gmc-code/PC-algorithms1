grade = "Acc"
match grade:
    case  "A+" | "A" | "B+" |  "B" | "C+" | "C":
        print("Acceptable standard.")
    case "D+" | "D" | "NP" | "UG":
        print("Retest required.")
    case other: 
        print(f"{other} entered")