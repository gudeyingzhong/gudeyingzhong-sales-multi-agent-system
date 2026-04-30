from openai import OpenAI
from config import MODEL_NAME, TEMPERATURE
from models import Lead

client = OpenAI()

def generate_followup(lead: Lead) -> str:
    prompt = f"""
你是销售跟进策略 Agent。

线索评分：{lead.score}
行业：{lead.industry}
预算：{lead.budget}
紧急度：{lead.urgency}

请输出：
1. 跟进目标
2. 推荐话术
3. 跟进节奏
"""

    resp = client.chat.completions.create(
        model=MODEL_NAME,
        temperature=TEMPERATURE,
        messages=[{"role": "user", "content": prompt}]
    )

    return resp.choices[0].message.content
