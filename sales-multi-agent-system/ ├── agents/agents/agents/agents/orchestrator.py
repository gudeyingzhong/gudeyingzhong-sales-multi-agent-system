from agents.lead_parser import parse_lead
from agents.lead_scorer import score_lead
from agents.followup_agent import generate_followup
from agents.human_handoff import need_human
from models import Lead

def run_pipeline(raw_message: str):
    lead = Lead(source="web_form", message=raw_message)
    lead = parse_lead(lead)
    lead = score_lead(lead)
    followup = generate_followup(lead)

    return {
        "lead": lead,
        "followup": followup,
        "handoff_to_human": need_human(lead)
    }
