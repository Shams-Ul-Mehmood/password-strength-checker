import re
import streamlit as stream_lite

stream_lite.set_page_config(page_title="Python Password Complexity Checker", page_icon="🔐")
stream_lite.title("🔐 Python Password Complexity Checker")
stream_lite.markdown("🔐 Password Complexity Checker helps you test password strength instantly — just enter" \
" your password 👉 get feedback 🔍 and tips 💡 like using 🔠 letters, 🔢 numbers & 🔣 symbols for a strong" \
" 🟢 password.")

user_password = stream_lite.text_input("Enter the password : ", type="password", key="password_input", placeholder="Please enter your password here.")

feedback = stream_lite.empty()
score = 0

if user_password:
    if len(user_password) > 10:
        score += 1
    else:
        feedback.append("📏Password length must be at least 10 characters long.🔢")
    
    if re.search(r"[a-z]", user_password) and re.search(r"[A-Z]", user_password):
        score += 1
    else:
        feedback.append("🔤Password must contain at least one uppercase and lowercase letters.🔠")
    
    if re.search(r"[0-9]", user_password):
        score += 1
    else:
        feedback.append("🔢Password should contain at least one number.🔢")
    
    if re.search(r"[!@#$%^&*()-_=+~`:;,.<>/?{}|\[]']", user_password):
        score += 1
    else:
        feedback.append("🔣 Password should contain at least one special character.🔣")
    
    if score == 4:
        feedback.append("✅Your password is strong!✅")
    elif score == 3:
        feedback.append("⚠️ Your password has medium level strength.🟡 It could be stronger.💪")
    elif score == 2:
        feedback.append("⚠️Your password has week level strength. 🔴 It could be stronger.💡")
    else:
        feedback.append("❌Your password is weak!❌")
    
    if feedback:
        stream_lite.markdown("🔑🚀📈✅Password Improvement Suggestions🧠🛠️💡🔧")
        for suggestion in feedback:
            stream_lite.write(suggestion)
    else:
        stream_lite.info("⚠️Please enter❗ a valid✅ password🔐 to check🔍 its strength🛡️.")