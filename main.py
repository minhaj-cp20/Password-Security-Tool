
import secrets
import string


print("========================================")
print("     Password Security Tool      ")
print("========================================")

password = input("Enter test Password: ")

password_lower = password.lower().





length = len(password)


if length < 8:
    length_result = "Too short"
elif length < 12:
    length_result = "Needs improvement"
else:
    length_result = "Good length"

print("\n================ Password Analysis ================")
print("Password Length =",length)






# step for checking the presence of uppercase, lowercase, numbers and special characters in the password    
    
has_upper = False
has_lower = False
has_number = False
has_special = False

for character in password:
    if character.isupper():
        has_upper = True
    elif character.islower():
        has_lower = True
    elif character.isdigit():
        has_number = True
    else:
        has_special = True
        
#check for common password words
common_passwords = [
    "password",
    "qwerty",
    "admin",
    "welcome",
    "letmein",
    "iloveyou",
    "123456"
]

is_common = False

for word in common_passwords:
    if word in password.lower():
        is_common = True
        break
    
    
predictable_patterns = [
    "1234", "2345", "3456", "4567",
    "abcd", "bcde", "cdef",
    "qwer", "asdf", "zxcv",
    "9876", "8765", "4321", "dcba"
]

has_predictable_pattern = False

for pattern in predictable_patterns:
    if pattern in password_lower:
        has_predictable_pattern = True
        break

has_repeated_pattern = False

for character in password:
    if character * 4 in password:
        has_repeated_pattern = True
        break
        
#for giving score based on the complexity of the password
score = 0
if length >= 16:
    score += 40
elif length >= 12:
    score +=30
elif length >= 8:
    score += 15

if has_upper:
    score += 15

if has_lower:
    score += 15
    
if has_number:
    score += 15 
    
if has_special:
    score += 15
    
#point deduction for common passwords, predictable patterns, and repeated patterns
    
    
if is_common:
    score -= 40

if has_predictable_pattern:
    score -= 25

if has_repeated_pattern:
    score -= 25

# Prevent negative scores
score = max(score, 0)

#displaying the score and complexity of the password
print("\n========== PASSWORD ANALYSIS ==========")
print("Password Length:", length)
print("Length Result:", length_result)
  
print ("\n================ Complexity Analysis ================")
print("Uppercase Letters :",has_upper)
print("Lowercase Letters :",has_lower)
print("Numbers :",has_number)
print("Special Characters:",has_special)

print("\n========== SECURITY CHECKS ==========")
print("Common Password Pattern:", is_common)
print("Predictable Sequence:", has_predictable_pattern)
print("Repeated Characters:", has_repeated_pattern)


print("\n=================STRENGTH ANALYSIS=================")
print("password Score :",score,"/100")


if length < 8:
    print("Password Strength: TOO SHORT")
elif is_common or has_predictable_pattern:
    print("Password Strength: WEAK - predictable pattern")
elif has_repeated_pattern:
    print("Password Strength: WEAK - repeated characters")
elif score >= 80:
    print("Password Strength: STRONG")
elif score >= 60:
    print("Password Strength: MODERATE")
else:
    print("Password Strength: WEAK")
    

# STEP 11: Password Improvement Recommendations

print("\n========== RECOMMENDATIONS ==========")

recommendations = []

if length < 12:
    recommendations.append(
        "Use a longer password, preferably 16 or more characters."
    )

if not has_upper:
    recommendations.append(
        "Include uppercase letters."
    )

if not has_lower:
    recommendations.append(
        "Include lowercase letters."
    )

if not has_number:
    recommendations.append(
        "Include numbers."
    )

if not has_special:
    recommendations.append(
        "Include special characters."
    )

if is_common:
    recommendations.append(
        "Avoid common password words and phrases."
    )

if has_predictable_pattern:
    recommendations.append(
        "Avoid predictable sequences such as 1234 or abcd."
    )

if has_repeated_pattern:
    recommendations.append(
        "Avoid repeating the same character four or more times."
    )

if recommendations:
    for recommendation in recommendations:
        print("-", recommendation)
else:
    print("No weaknesses detected by these basic checks.")
   
print("\nAnalysis Completed")


# STEP 9: Strong Password Generator

print("\n========== PASSWORD GENERATOR ==========")

choice = input(
    "Would you like to generate a password? (yes/no): "
).strip().lower()

if choice == "yes":

    length_input = input("Enter password length (12-64): ")

    if length_input.isdigit():

        password_length = int(length_input)

        if 12 <= password_length <= 64:

           
            
            
            # STEP 10: Analyze the generated password

            generated_lower = new_password.lower()
            generated_length = len(new_password)

            generated_upper = any(c.isupper() for c in new_password)
            generated_lowercase = any(c.islower() for c in new_password)
            generated_number = any(c.isdigit() for c in new_password)
            generated_special = any(
                not c.isalnum() for c in new_password
            )

            generated_common = any(
                word in generated_lower for word in common_passwords
            )

            generated_predictable = any(
                pattern in generated_lower
                for pattern in predictable_patterns
            )

            generated_repeated = any(
                c * 4 in new_password for c in new_password
            )

            # Calculate the generated password score
            generated_score = 0

            if generated_length >= 16:
                generated_score += 40
            elif generated_length >= 12:
                generated_score += 30
            elif generated_length >= 8:
                generated_score += 15

            if generated_upper:
                generated_score += 15
            if generated_lowercase:
                generated_score += 15
            if generated_number:
                generated_score += 15
            if generated_special:
                generated_score += 15

            if generated_common:
                generated_score -= 40
            if generated_predictable:
                generated_score -= 25
            if generated_repeated:
                generated_score -= 25

            generated_score = max(generated_score, 0)

            # Display the analysis
            print("\n========== GENERATED PASSWORD ANALYSIS ==========")
            print("Uppercase:", generated_upper)
            print("Lowercase:", generated_lowercase)
            print("Numbers:", generated_number)
            print("Special characters:", generated_special)
            print("Common password pattern:", generated_common)
            print("Predictable sequence:", generated_predictable)
            print("Repeated characters:", generated_repeated)
            print("Strength score:", generated_score, "/100")

            if generated_common or generated_predictable or generated_repeated:
                print("Result: Contains a detected weakness")
            elif generated_score >= 80:
                print("Result: STRONG according to current rules")
            elif generated_score >= 60:
                print("Result: MODERATE")
            else:
                print("Result: WEAK")

        else:
            print("Enter a length between 12 and 64.")

    else:
        print("Please enter a valid whole number.")

elif choice == "no":
    print("Password generation skipped.")

else:
    print("Please enter yes or no.")



