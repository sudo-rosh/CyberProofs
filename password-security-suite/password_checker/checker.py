def check_length(password):
    if len(password) < 8:
        return (False)
    return (True)

def check_upper_lower(password):
    if not any(char.isupper() for char in password):
        return(False)
    if not any(char.islower() for char in password):
        return(False)
    return(True)

def check_numbers(password):
    if not any(char.isdigit() for char in password):
        return(False)
    return(True)

def check_special_characters(password):
    special_characters = "!@#$%^&*()-+"
    if not any(char in special_characters for char in password):
        return(False)
    return(True)

def rate_password(password):
    score = 0
    if check_length(password):
        score += 1
    if check_upper_lower(password):
        score += 1
    if check_numbers(password):
        score += 1
    if check_special_characters(password):
        score += 1
    
    if score == 4:
        return("Very Strong")
    if score == 3:
        return("Strong")
    if score == 2:
        return("Moderate")
    if score == 1:
        return("Weak")
    return("Very Weak")
