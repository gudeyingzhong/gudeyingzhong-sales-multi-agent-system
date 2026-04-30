from openai import OpenAI
from config import MODEL_NAME, TEMPERATURE
from models import Lead

client = OpenAI()

def score_lead(lead: Lead) -> Lead:
    prompt = f"""
你是销售评分 Agent，请进行推理。

行业：{lead.industry}
预算：{lead.budget}
紧急度：{lead.urgency}
客户消息：{lead.message}

请给出 0-100 的整数分数。
只返回数字。
"""

    resp = client.chat.completions.create(
        model=MODEL_NAME,
        temperature=TEMPERATURE,
        messages=[{"role": "user", "content": prompt}]
    )

    lead.score = int(resp.choices[0].message.content.strip())
    return lead
