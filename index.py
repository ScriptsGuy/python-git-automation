import subprocess


def run(*args):

    return subprocess.check_call(["git"] + list(args))


def commit():
    run("add", ".")
    message = input("\nType in your commit message: ")
    commit_message = f"{message}"
    run("commit", "-m", commit_message)
    run("push", "-u", "origin", "master")


commit()
