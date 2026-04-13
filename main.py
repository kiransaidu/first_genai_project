from code_generator import generate_code
from file_handler import apply_code
from git_handler import clone, create_branch, setup_repo, push_code
from util import get_branch

def main():

    task = input("Enter task: ")

    # Generate code
    res = generate_code(task)
    file = res["file"]
    code = res["code"]

    print("Generated file:", file)
    print("Generated code:", code)

    # Git operations
    clone()
    setup_repo()

    # ✅ CREATE BRANCH
    branch_name = get_branch()
    create_branch(branch_name)

    
    # Apply code
    apply_code(".", file, code)

    # Push to GitHub
   # ✅ PUSH TO BRANCH
    push_code(branch_name)

    print(f" Code pushed to branch: {branch_name}")

main()