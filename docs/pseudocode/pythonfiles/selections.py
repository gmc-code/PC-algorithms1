is_raining = False
is_cold = False
print("Good Morning.")
if is_raining and is_cold:
    print("Bring Umbrella and jacket.")
elif is_raining and not(is_cold):
    print("Bring Umbrella.")
elif not(is_raining) and is_cold:
    print("Bring Jacket.")
else:
    print("Wear a sun hat.")


# BEGIN
# is_raining ← False
# is_cold ← False
# OUTPUT "Good Morning."
# IF is_raining AND is_cold THEN
#     OUTPUT "Bring Umbrella and jacket."
# ELSEIF is_raining AND NOT(is_cold) THEN
#     OUTPUT "Bring Umbrella."
# ELSEIF NOT(is_raining) AND is_cold THEN
#     OUTPUT "Bring Jacket."
# ELSE
#     OUTPUT "Wear a sun hat."
# ENDIF
# END
