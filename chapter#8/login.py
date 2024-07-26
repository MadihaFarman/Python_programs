def get_login_name(firstName,lastName,idNumber):
    set_1 = firstName[0:3]
    set_2 = lastName[0:3]
    set_3 = idNumber[-3:]
    login_name = set_1 + set_2 + set_3
    return login_name
# The following code checks the validity of a password
def valid_password(password):
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    if len(password)>=7:
        correct_length = True
        for ch in password:
            if ch.isupper():
                has_uppercase = True
            if ch.islower():
                has_lowercase = True
            if ch.isdigit():
                has_digit = True
    if correct_length and has_uppercase and has_lowercase and has_digit:
        is_valid = True
    else:
        is_valid = False
    return is_valid
        
                 

