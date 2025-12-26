# Simple tool to check if a password is long enough for security
def check_security(password):
    if len(password) >= 8:
        return "Password meets length requirements."
    else:
        return "Password is too short for security standards."

# Testing the tool
print(check_security("GiftTech2025"))
