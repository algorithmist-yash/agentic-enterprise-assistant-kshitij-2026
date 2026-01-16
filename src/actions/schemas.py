from pydantic import BaseModel
from typing import List, Optional


class ScheduleMeeting(BaseModel):
    action: str = "schedule_meeting"
    department: str
    date: str
    time: str
    participants: Optional[List[str]] = ["user"]


class CreateTicket(BaseModel):
    action: str = "create_support_ticket"
    issue_type: str
    description: str
    priority: str = "medium"
