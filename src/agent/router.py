import re
from src.actions.schemas import ScheduleMeeting, CreateTicket

import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


def classify_intent(user_input: str) -> str:
    user_input = user_input.lower()

    if any(word in user_input for word in ["schedule", "meeting", "book"]):
        return "schedule_meeting"

    if any(word in user_input for word in ["ticket", "issue", "problem", "support"]):
        return "create_ticket"

    return "information"


def handle_action(user_input: str):
    intent = classify_intent(user_input)

    if intent == "schedule_meeting":
        return ScheduleMeeting(
            department="HR",
            date="2026-01-18",
            time="11:00"
        ).model_dump()

    if intent == "create_ticket":
        return CreateTicket(
            issue_type="IT Access",
            description=user_input,
            priority="high"
        ).model_dump()

    return None
