from orchestrator import run_pipeline

if __name__ == "__main__":
    message = """
我们是一家 50 人左右的 SaaS 公司，
需要 CRM 自动化方案，
预算 10 万 / 年，
希望 1 个月内上线。
"""

    result = run_pipeline(message)

    print("线索评分:", result["lead"].score)
    print("是否转人工:", result["handoff_to_human"])
    print("跟进建议:")
    print(result["followup"])
