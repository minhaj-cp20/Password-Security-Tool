
from flask import Flask, render_template, request
import string
import secrets

app = Flask(__name__)

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(
        secrets.choice(characters) for _ in range(length)
    )

    return password


@app.route("/generate-password")
def generate_password_route():
    length = request.args.get("length", default=16, type=int)

    if length not in [8,12, 16,  24]:
        length = 16

    password = generate_password(length)
    return {"password": password}


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze",methods=["POST"])
def analyze():
    password = request.form.get("password","")
    if not password:
        return render_template("index.html", error="Please enter a valid password.")
    password_length = len(password)
    
    score =0
    
    if password_length >= 8:
        score += 20
    
    if password_length >= 12:
        score += 20
    
    
    has_uppercase = any(char.isupper() for char in password)
    
    has_lowercase = any(char.islower() for char in password)
    
    has_digit = any(char.isdigit() for char in password)
    
    has_special = any(not char.isalnum() for char in password)
    
    if has_uppercase:
        score += 15
        
    if has_lowercase:
        score += 15
        
    if has_digit:
        score += 15
        
    if has_special:
        score += 15
        
        
        
    if score < 40:
        strength ="weak"
    
    elif score < 70:
        strength  = "moderate"
        
    else:
        strength = "strong"

    
    if password_length < 8:
        length_result = "Too short"
    elif password_length < 12:
        length_result = "Needs improvement"
    else:
        length_result = "Strong password"   
        
        
    recommendations = []
    if password_length < 12:
        recommendations.append("Use atleast 12 characters.")
        
    if not has_uppercase:
        recommendations.append("Include uppercase letters.")
        
    if not has_lowercase:
        recommendations.append("Include lowercase letters.")    
        
    if not has_digit: 
        recommendations.append("Include digits.")
        
    if not has_special:
        recommendations.append("Include special characters.")

    return render_template(
        "index.html",
        result=(f"password length: {password_length} characters - {length_result}.\n"
                f"uppercase present: {has_uppercase}.\n"
                f"lowercase present: {has_lowercase}.\n"
                f"digit present: {has_digit}.\n"
                f"special character present: {has_special}."),
        score=score,
        strength=strength,
        recommendations=recommendations
    ) 

if __name__ == "__main__":
    app.run(debug=True)