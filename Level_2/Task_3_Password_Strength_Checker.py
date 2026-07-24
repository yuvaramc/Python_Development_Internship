import string

def password_strength_checker():
    password = input("Enter your password: ")

    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    score = 0

    if length >= 8:
        score += 1

    if has_upper:
        score += 1

    if has_lower:
        score += 1

    if has_digit:
        score += 1

    if has_special:
        score += 1

    print("\nPassword Analysis:")
    print("Length:", "✔" if length >= 8 else "✘")
    print("Uppercase letter:", "✔" if has_upper else "✘")
    print("Lowercase letter:", "✔" if has_lower else "✘")
    print("Digit:", "✔" if has_digit else "✘")
    print("Special character:", "✔" if has_special else "✘")

    if score == 5:
        print("\n🔒 Strong Password")
    elif score >= 3:
        print("\n⚠️ Medium Password")
    else:
        print("\n❌ Weak Password")

password_strength_checker()