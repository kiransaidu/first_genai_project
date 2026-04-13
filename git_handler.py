import os
from app_config import REPO_URL, BASE_BRANCH

def run(cmd):
    print(f"Running: {cmd}")
    os.system(cmd)

def clone():
    if not os.path.exists("repo"):
        run(f"git clone {REPO_URL} repo")

def setup_repo():
    os.chdir("repo")

    run(f"git checkout {BASE_BRANCH}")
    run("git pull")

def push_code(branch_name):
    run("git add .")
    run('git commit -m "AI generated code" || echo "No changes"')
    run(f"git push -u origin {branch_name}")

def create_branch(branch_name):
    run(f"git checkout {BASE_BRANCH}")
    run("git pull")

    # Create new branch
    run(f"git checkout -b {branch_name}")    