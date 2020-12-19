import subprocess

origin = "https://github.com/devzonedz/python-git-automation.git"

push_url = "https://devzonedz:DevZoneGit2020@github.com/devzonedz/python-git-automation.git"


def run(*args):

    return subprocess.check_call(["git"] + list(args))


def commit():
    run("add", ".")
    # run("remote", "add", "origin", origin)
    # run("remote", "set-url", "origin", origin)
    message = input("\nType in your commit message: ")
    commit_message = f"{message}"
    run("commit", "-am", commit_message)
    # run("push", "--set-upstream", push_url, "master")
    run("push", push_url)


commit()
