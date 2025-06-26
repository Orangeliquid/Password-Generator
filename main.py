from utils.generator import generate_password
from utils.prompt import prompt_user_options
from utils.strength import evaluate_strength

opts = prompt_user_options()
if opts:
    password = generate_password(options=opts)
    strength, label = evaluate_strength(password=password)

    print(f"Generated Password: {password}\nStrength: {label}, {strength}")
