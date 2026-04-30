from openai import OpenAI
from config import MODEL_NAME, TEMPERATURE
from models import Lead
import json

client = OpenAI()

def parse_lead(lead: Lead) -> Lead:
    prompt = f"""
你是销售线索理解 Agent。
请从以下客户消息中提取：
- 行业
- 预算水平（低 / 中 / 高 / 未知）
- 紧急度（低 / 中 / 高）

客户消息：
{lead.message}

只返回 JSON。
"""

    resp = client.chat.completions.create(
        model=MODEL_NAME,
        temperature=TEMPERATURE,
        messages=[{"role": "user", "content": prompt}]
    )

    data = json.loads(resp.choices[0].message.content)
    lead.industry = data.get("行业")
    lead.budget = data.get("预算水平")
    lead.urgency = data.get("紧急度")
    return lead
