import re

def assess_password_strength(password):
    # Criteria flags
    length_flag = len(password) >= 8
    lowercase_flag = re.search(r"[a-z]", password) is not None
    uppercase_flag = re.search(r"[A-Z]", password) is not None
    digit_flag = re.search(r"\d", password) is not None
    special_char_flag = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    # Feedback messages
    feedback = []

    if length_flag:
        feedback.append("✓ Password length is sufficient (8 characters or more)")
    else:
        feedback.append("✗ Password length should be at least 8 characters")

    if lowercase_flag:
        feedback.append("✓ Contains lowercase letters")
    else:
        feedback.append("✗ Should contain lowercase letters")

    if uppercase_flag:
        feedback.append("✓ Contains uppercase letters")
    else:
        feedback.append("✗ Should contain uppercase letters")

    if digit_flag:
        feedback.append("✓ Contains digits")
    else:
        feedback.append("✗ Should contain digits")

    if special_char_flag:
        feedback.append("✓ Contains special characters")
    else:
        feedback.append("✗ Should contain special characters")

    # Determine strength
    strength = sum([length_flag, lowercase_flag, uppercase_flag, digit_flag, special_char_flag])
    strength_levels = {
        5: "Very Strong",
        4: "Strong",
        3: "Moderate",
        2: "Weak",
        1: "Very Weak",
        0: "Very Weak"
    }

    strength_message = strength_levels[strength]
    return strength_message, feedback

def main():
    password = input("Enter your password: ")
    strength, feedback = assess_password_strength(password)
    
    print("\nPassword Strength:", strength)
    print("Feedback:")
    for message in feedback:
        print(message)

if __name__ == "__main__":
    main()
