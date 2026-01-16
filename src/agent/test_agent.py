import os
import sys

# -----------------------------
# FIX PYTHON PATH (WINDOWS SAFE)
# -----------------------------
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# -----------------------------
# NOW IMPORTS WILL WORK
# -----------------------------
from src.agent.router import handle_action


if __name__ == "__main__":
    queries = [
        "Schedule a meeting with HR tomorrow at 11 AM",
        "Create a support ticket for VPN access",
        "What are the key risks mentioned in the report?"
    ]

    for q in queries:
        print("\nUSER:", q)
        result = handle_action(q)
        print("AGENT OUTPUT:", result)
