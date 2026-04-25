"""Euru OS — Automatic Git Sync after report generation."""
import subprocess
import datetime
import os

REPO_DIR = os.path.dirname(os.path.abspath(__file__))

def git_sync(description="auto-sync after report generation"):
    """Stage all changes, commit with timestamp, and push to origin main."""
    try:
        ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        msg = f"Euru OS — {ts} — {description}"
        subprocess.run(["git", "add", "-A"], cwd=REPO_DIR, check=True, capture_output=True)
        result = subprocess.run(
            ["git", "status", "--porcelain"], cwd=REPO_DIR, capture_output=True, text=True
        )
        if not result.stdout.strip():
            print("[git-sync] Nothing to commit.")
            return
        subprocess.run(["git", "commit", "-m", msg], cwd=REPO_DIR, check=True, capture_output=True)
        subprocess.run(["git", "push", "origin", "main"], cwd=REPO_DIR, check=True, capture_output=True)
        print(f"[git-sync] Pushed: {msg}")
    except subprocess.CalledProcessError as e:
        print(f"[git-sync] WARNING: git sync failed — {e}")
    except FileNotFoundError:
        print("[git-sync] WARNING: git not found in PATH")
