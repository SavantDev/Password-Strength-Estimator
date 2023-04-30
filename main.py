import re

def password_strength(password):
    """Estimates the strength of a password on a scale of 1 to 5."""

    if len(password) < 8:
        return 1

    if re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password):
        return 5
 
    if re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9@#$%^&+=])[A-Za-z\d@#$%^&+=]{8,}$', password):
        return 4
    
    if re.match(r'^[a-z]+$|^\d+$', password):
        return 2
      
    return 3

password = input("Enter a password and I will estimate its strength: ")
strength = password_strength(password)

if strength == 1:
    print("This is a very weak password.")
elif strength == 2:
    print("This is a weak password.")
elif strength == 3:
    print("This is a password of average strength.")
elif strength == 4:
    print("This is a moderately strong password.")
else:
    print("This is a strong password.")
