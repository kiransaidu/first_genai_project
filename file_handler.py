import os

def apply_code(base_path, file, code):
    full_path = os.path.join(base_path, file)

    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(code)

    print(f"✅ Code written to {full_path}")