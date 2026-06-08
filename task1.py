import re
import secrets
import string

def calculate_score(password):
    length = len(password)
    
    if length == 0:
        return 1
    if length < 8:
        return 1  
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    
    diversity_count = sum([has_upper, has_lower, has_digit, has_special])
    if length >= 12 and diversity_count == 4:
        return 5  
    elif length >= 12 and diversity_count >= 3:
        return 4  
    elif length >= 10 and diversity_count >= 3:
        return 3  
    elif length >= 8 and diversity_count >= 2:
        return 2  
    else:
        return 1  

def analyze_password(password):
    feedback = []
    if not re.search(r"[A-Z]", password): feedback.append("Add uppercase letters.")
    if not re.search(r"[a-z]", password): feedback.append("Add lowercase letters.")
    if not re.search(r"\d", password): feedback.append("Add numbers.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): feedback.append("Add special characters.")
    if len(password) < 12: feedback.append("Make it longer (ideally 12+ characters).")

    score = calculate_score(password)
    rating_map = {
        1: "Very Weak",
        2: "Weak",
        3: "Moderate",
        4: "Strong",
        5: "Very Strong"
    }
    
    return score, rating_map[score], feedback

def generate_strong_password(length=16):
    password = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice("!@#$%^&*")
    ]
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password += [secrets.choice(all_chars) for _ in range(length - 4)]
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

if __name__ == "__main__":
    pwd = input("Enter a password to analyze: ").strip()
    
    if not pwd:
        print("You didn't enter anything!")
    else:
        score, rating, feedback = analyze_password(pwd)
        bar = " ".join(["■" if i < score else "□" for i in range(5)])
        
        print("\n" + "="*30)
        print(f"Strength Level: {score} / 5")
        print(f"Scale:          [{bar}] ({rating})")
        print("="*30)
        
        if feedback and score < 5:
            print("\nSuggestions to improve:")
            for item in feedback:
                print(f" • {item}")
        else:
            print("\n✨ Excellent choice! Your password meets top security standards. ✨")

        if score < 4:
            print(f"\n💡 Security Tip: Try this Level 5 password instead:\n   {generate_strong_password()}")
