# detector/schema.py

MESSAGE_TYPES = [
    "minimal_greeting",
    "who_are_you",
    "confirms_business",
    "wrong_number",
    "not_owner",
    "asks_human",
    "pricing_question",
    "demo_request",
    "whatsapp_question",
    "menu_question",
    "reservation_question",
    "objection",
    "rejection",
    "opt_out",
    "support",
    "sensitive_case",
    "unknown",
]


TONES = [
    "neutral",
    "curious",
    "interested",
    "distrustful",
    "confused",
    "rushed",
    "annoyed",
    "aggressive",
]


SENTIMENTS = [
    "positive",
    "neutral",
    "negative",
    "mixed",
]


CONTACT_ROLES = [
    "owner",
    "manager",
    "employee",
    "third_party",
    "unknown",
]


LEAD_STATES = [
    "new",
    "number_validation_pending",
    "number_validated",
    "responsible_validation_pending",
    "responsible_confirmed",
    "proposal_ready",
    "interested",
    "with_objection",
    "demo_requested",
    "demo_pending",
    "support_needed",
    "not_interested",
    "opt_out",
    "human_review",
]


OBJECTIONS = [
    "spam_distrust",
    "privacy_data",
    "price",
    "already_has_instagram",
    "already_has_website",
    "already_has_google_maps",
    "no_time",
    "not_decision_maker",
    "does_not_understand_offer",
    "fear_wrong_publication",
    "none",
]


RISK_LEVELS = [
    "low",
    "medium",
    "high",
]


NEXT_STEPS = [
    "ask_clarification",
    "validate_business_number",
    "validate_responsible_person",
    "explain_montserrat",
    "present_short_proposal",
    "answer_objection",
    "offer_demo_or_preview",
    "send_to_human",
    "register_opt_out",
    "close_politely",
    "schedule_followup",
    "ask_minimum_data",
]