from dataclasses import dataclass

@dataclass
class Lead:
    source: str
    message: str
    industry: str | None = None
    budget: str | None = None
    urgency: str | None = None
    score: int | None = None
