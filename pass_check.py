import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_criteria = re.search(r'[@$!%*?&]', password) is not None
    
    score = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])
    
    if score < 3:
        return "Weak password. Consider using a longer password with a mix of characters."
    elif score == 3:
        return "Moderate password. Try adding more variety in characters."
    else:
        return "Strong password!"

if __name__ == "__main__":
    user_password = input("Enter a password to check its strength: ")
    print(check_password_strength(user_password))
