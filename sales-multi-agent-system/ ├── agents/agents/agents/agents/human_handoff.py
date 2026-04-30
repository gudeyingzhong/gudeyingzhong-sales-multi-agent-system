from models import Lead

def need_human(lead: Lead) -> bool:
    return lead.score >= 75
