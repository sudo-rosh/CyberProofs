from password_checker.checker import * #This is used to call functions from other python files

while True:
    password = input("Enter your password: ")

    #Password Strength Checker

    score, rating = rate_password(password)
    print(f"Your password strength is: {rating} ({score}/4)")

    if not check_length(password):
        print("→ Password must be at least 8 characters")
    if not check_upper_lower(password):
        print("→ Password must contain both uppercase and lowercase letters")
    if not check_numbers(password):
        print("→ Password must contain at least one number")
    if not check_special_characters(password):
        print("→ Password must contain at least one special character")