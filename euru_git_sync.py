"""Euru OS - Automatic Git Sync after report generation."""
import subprocess
import datetime
import os

REPO_DIR = os.path.dirname(os.path.abspath(__file__))


def _run(args):
    return subprocess.run(args, cwd=REPO_DIR, check=True, capture_output=True, text=True)


def _current_branch():
    result = _run(["git", "branch", "--show-current"])
    return result.stdout.strip() or "main"


def _has_origin():
    result = subprocess.run(
        ["git", "remote", "get-url", "origin"],
        cwd=REPO_DIR,
        capture_output=True,
        text=True,
    )
    return result.returncode == 0 and bool(result.stdout.strip())


def git_sync(description="auto-sync after report generation"):
    """Stage changes, commit locally, and push only when origin is configured."""
    try:
        ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        msg = f"Euru OS - {ts} - {description}"
        _run(["git", "add", "-A"])
        result = subprocess.run(
            ["git", "status", "--porcelain"], cwd=REPO_DIR, capture_output=True, text=True
        )
        if not result.stdout.strip():
            print("[git-sync] Nothing to commit.")
            return
        _run(["git", "commit", "-m", msg])
        branch = _current_branch()
        if _has_origin():
            _run(["git", "push", "origin", branch])
            print(f"[git-sync] Pushed {branch}: {msg}")
        else:
            print(f"[git-sync] Committed locally on {branch}; no origin remote configured.")
    except subprocess.CalledProcessError as e:
        print(f"[git-sync] WARNING: git sync failed - {e}")
    except FileNotFoundError:
        print("[git-sync] WARNING: git not found in PATH")
