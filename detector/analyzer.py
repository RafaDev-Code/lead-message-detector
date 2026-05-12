from detector.rules import detect_by_rules
from detector.extractor import extract_data
from detector.brief import build_do_not_do

def analyze_lead_message(
    conversation: str,
    last_message: str,
    current_state: str | None = None,
    business_context: str | None = None,
) -> dict:

    normalized_message = last_message.lower().strip()

    extracted_data = extract_data(normalized_message)

    base_result = {
        "message_type": "unknown",
        "tone": "neutral",
        "sentiment": "neutral",
        "lead_state_suggestion": current_state or "new",
        "contact_role": "unknown",
        "intent": "unknown",
        "objection": "none",
        "interests": [],
        "risk_level": "low",
        "human_review_required": False,

        "extracted_data": extracted_data,

        "evidence": [],
        "next_step": "ask_clarification",
        "sales_agent_brief": "No se detectó una intención clara. Conviene pedir aclaración breve.",
        "suggested_reply": "Perdón, para entender bien: ¿me decís si hablás por el local?",
        "crm_payload": {
            "commercial_state": current_state or "new",
            "role": "unknown",
            "tags": [],
            "note": "Mensaje sin clasificación clara.",
        },
    }

    rule_result = detect_by_rules(normalized_message)

    if rule_result is not None:
        base_result.update(rule_result)

    base_result["do_not_do"] = build_do_not_do(base_result)

    return base_result
