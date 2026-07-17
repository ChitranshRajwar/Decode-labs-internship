print("=" * 35)
print("   PASSWORD STRENGTH CHECKER")
print("=" * 35)

password = input("Enter your password: ")

score = 0

if len(password) >= 8:
    score += 1
else:
    print("Password should be at least 8 characters long.")

has_upper = False
for ch in password:
    if ch.isupper():
        has_upper = True
        break

if has_upper:
    score += 1
else:
    print("Add at least one uppercase letter.")

has_lower = False
for ch in password:
    if ch.islower():
        has_lower = True
        break

if has_lower:
    score += 1
else:
    print("Add at least one lowercase letter.")

has_digit = False
for ch in password:
    if ch.isdigit():
        has_digit = True
        break

if has_digit:
    score += 1
else:
    print("Add at least one number.")

special = "!@#$%^&*"
has_special = False

for ch in password:
    if ch in special:
        has_special = True
        break

if has_special:
    score += 1
else:
    print("Add at least one special character.")

common_passwords = ["password", "123456", "admin", "qwerty"]

if password.lower() not in common_passwords:
    score += 1
else:
    print("This is a common password. Choose another one.")

print("\nScore:", score, "/6")

if score <= 2:
    print("Password Strength: Weak")
elif score <= 4:
    print("Password Strength: Moderate")
else:
    print("Password Strength: Strong")
