from pathlib import Path  # Python 3.6+ only
from dotenv import load_dotenv
import subprocess
import os

load_dotenv()

load_dotenv(verbose=True)

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


password = os.getenv("PERSONAL_PASSWORD", "password not found")


# origin = "https://github.com/devzonedz/python-git-automation.git"

push_url = f"https://ScriptsGuy:{password}@github.com/ScriptsGuy/python-git-automation.git"


def run(*args):
    return subprocess.check_call(["git"] + list(args))


def commit():
    run("add", ".")
    # run("remote", "add", "origin", origin)
    # run("remote", "set-url", "origin", origin)
    message = input("\nType in your commit message: ")
    commit_message = f"{message}"
    run("commit", "-am", commit_message)
    run("push", "--set-upstream", push_url, "master")
    # run("push", push_url)


commit()
