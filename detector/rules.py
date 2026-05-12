from detector.objetion_classifier import detect_objection_detail
from detector.rule_sets import (
    OPT_OUT_KEYWORDS,
    SENSITIVE_KEYWORDS,
    ASKS_HUMAN_KEYWORDS,
    SUPPORT_KEYWORDS,
    REJECTION_KEYWORDS,
    WRONG_NUMBER_KEYWORDS,
    NOT_OWNER_KEYWORDS,
    CONFIRMS_BUSINESS_KEYWORDS,
    WHO_ARE_YOU_KEYWORDS,
    WHATSAPP_QUESTION_KEYWORDS,
    MENU_QUESTION_KEYWORDS,
    RESERVATION_QUESTION_KEYWORDS,
    OBJECTION_KEYWORDS,
    PRICING_KEYWORDS,
    DEMO_KEYWORDS,
    GREETING_KEYWORDS,
)


def find_matches(text: str, keywords: list[str]) -> list[str]:
    matches = []

    for keyword in keywords:
        if keyword in text:
            matches.append(keyword)
    return matches

def detect_by_rules(message: str) -> dict :


    #OPT-OUT - Caso Sensible
    matches = find_matches(message, OPT_OUT_KEYWORDS)
    if matches:
        return {
            "message_type": "opt_out",
            "tone": "annoyed",
            "sentiment": "negative",
            "lead_state_suggestion": "opt_out",
            "contact_role": "unknown",
            "intent": "stop_contact",
            "objection": "none",
            "interests": ["opt_out_requested"],
            "risk_level": "high",
            "human_review_required": True,
            "evidence": matches,
            "next_step": "register_opt_out",
            "sales_agent_brief": "El lead pidió no ser contactado. No vender, no insistir y registrar opt-out.",
            "suggested_reply": "Entendido, no volvemos a contactarte. Gracias.",
            "crm_payload": {
                "commercial_state": "opt_out",
                "role": "unknown",
                "tags": ["opt_out_requested"],
                "note": "Lead pidió no recibir más mensajes.",
            },
        }


    #Casos Sensibles y/o Agresivos
    matches = find_matches(message, SENSITIVE_KEYWORDS)
    if matches:
        return {
            "message_type": "sensitive_case",
            "tone": "aggressive",
            "sentiment": "negative",
            "lead_state_suggestion": "human_review",
            "contact_role": "unknown",
            "intent": "raise_sensitive_complaint",
            "objection": "spam_distrust",
            "interests": [],
            "risk_level": "high",
            "human_review_required": True,
            "evidence": matches,
            "next_step": "send_to_human",
            "sales_agent_brief": "El lead muestra agresión, amenaza o acusa posible estafa. No vender. Derivar a humano y responder con cuidado.",
            "suggested_reply": "Entiendo. No queremos generar molestias. Muchas gracias.",
            "crm_payload": {
                "commercial_state": "human_review",
                "role": "unknown",
                "tags": ["sensitive_case", "possible_spam_perception"],
                "note": "Lead expresó agresión, amenaza o desconfianza fuerte."
            },
        }


    #Pide Comunicación con Humano
    matches = find_matches(message, ASKS_HUMAN_KEYWORDS)

    if matches:
        return {
            "message_type": "asks_human",
            "tone": "neutral",
            "sentiment": "neutral",
            "lead_state_suggestion": "human_review",
            "contact_role": "unknown",
            "intent": "request_human",
            "objection": "none",
            "interests": [],
            "risk_level": "medium",
            "human_review_required": True,
            "evidence": matches,
            "next_step": "send_to_human",
            "sales_agent_brief": "El lead pidió hablar con una persona. No seguir automatizando la venta.",
            "suggested_reply": "Sí, te paso con una persona del equipo.",
            "crm_payload": {
                "commercial_state": "human_review",
                "role": "unknown",
                "tags": ["human_requested"],
                "note": "Lead pidió hablar con una persona.",
            },
        }


    #Pide soporte
    matches = find_matches(message, SUPPORT_KEYWORDS)
    if matches:
        return {
            "message_type": "support",
            "tone": "confused",
            "sentiment": "negative",
            "lead_state_suggestion": "support_needed",
            "contact_role": "unknown",
            "intent": "request_support",
            "objection": "none",
            "interests": ["support_request"],
            "risk_level": "high",
            "human_review_required": True,
            "evidence": matches,
            "next_step": "send_to_human",
            "sales_agent_brief": "El lead parece necesitar soporte. No vender. Derivar a una persona o canal de soporte.",
            "suggested_reply": "Entiendo. Esto lo revisa una persona del equipo para ayudarte bien.",
            "crm_payload": {
                "commercial_state": "support_needed",
                "role": "unknown",
                "tags": ["support_request"],
                "note": "Lead manifestó un problema o pidió soporte.",
            },
        }


    #Rechazo indirecto
    matches = find_matches(message, REJECTION_KEYWORDS)
    if matches:
        return {
            "message_type": "rejection",
            "tone": "neutral",
            "sentiment": "negative",
            "lead_state_suggestion": "not_interested",
            "contact_role": "unknown",
            "intent": "reject_offer",
            "objection": "none",
            "interests": [],
            "risk_level": "medium",
            "human_review_required": False,
            "evidence": matches,
            "next_step": "close_politely",
            "sales_agent_brief": "El lead rechazó la propuesta. No insistir. Cerrar amable.",
            "suggested_reply": "Entendido, gracias por responder. Que tengas buen día.",
            "crm_payload": {
                "commercial_state": "not_interested",
                "role": "unknown",
                "tags": ["not_interested"],
                "note": "Lead rechazó la propuesta.",
            },
        }


    #Numero equivocado
    matches = find_matches(message, WRONG_NUMBER_KEYWORDS)
    if matches:
        return {
            "message_type": "wrong_number",
            "tone": "neutral",
            "sentiment": "neutral",
            "lead_state_suggestion": "number_validation_pending",
            "contact_role": "unknown",
            "intent": "report_wrong_number",
            "objection": "none",
            "interests": [],
            "risk_level": "medium",
            "human_review_required": False,
            "evidence": matches,
            "next_step": "validate_business_number",
            "sales_agent_brief": "El lead indica que podría ser número equivocado. Conviene validar antes de seguir.",
            "suggested_reply": "Gracias por avisar. Puede que tengamos mal cargado el número, disculpá la molestia.",
            "crm_payload": {
                "commercial_state": "number_validation_pending",
                "role": "unknown",
                "tags": ["wrong_number"],
                "note": "Lead indicó posible número equivocado.",
            },
        }


    # No es dueño / no es responsable
    matches = find_matches(message, NOT_OWNER_KEYWORDS)
    if matches:
        return {
            "message_type": "not_owner",
            "tone": "neutral",
            "sentiment": "neutral",
            "lead_state_suggestion": "responsible_validation_pending",
            "contact_role": "employee",
            "intent": "declare_not_decision_maker",
            "objection": "not_decision_maker",
            "interests": [],
            "risk_level": "medium",
            "human_review_required": False,
            "evidence": matches,
            "next_step": "validate_responsible_person",
            "sales_agent_brief": "La persona indica que no es quien decide. Conviene pedir contacto del responsable sin presionar.",
            "suggested_reply": "Gracias por aclararlo. ¿Sabés quién ve estos temas del local?",
            "crm_payload": {
                "commercial_state": "responsible_validation_pending",
                "role": "employee",
                "tags": ["not_decision_maker"],
                "note": "Lead indicó que no es responsable de la decisión.",
            },
        }


    # Detecta cuando la persona confirma que estamos hablando con el negocio correcto.
    matches = find_matches(message, CONFIRMS_BUSINESS_KEYWORDS)

    if matches:
        return {
            "message_type": "confirms_business",
            "tone": "neutral",
            "sentiment": "neutral",
            "lead_state_suggestion": "number_validated",
            "intent": "confirm_business_number",
            "objection": "none",
            "interests": [],
            "risk_level": "low",
            "human_review_required": False,
            "evidence": matches,
            "next_step": "validate_responsible_person",
            "sales_agent_brief": "El lead confirmó que es el local. Falta validar si habla con la persona responsable.",
            "suggested_reply": "Perfecto, gracias. ¿Sos quien maneja estos temas del local?",

            "crm_payload": {
                "commercial_state": "number_validated",
                "role": "unknown",
                "tags": ["business_confirmed"],
                "note": "Lead confirmó que el número corresponde al local.",
            },
        }


    # Detecta si el lead pregunta por WhatsApp como canal.
    matches = find_matches(message, WHATSAPP_QUESTION_KEYWORDS)
    if matches:
        return {
            "message_type": "whatsapp_question",
            "tone": "curious",
            "sentiment": "neutral",
            "lead_state_suggestion": "interested",
            "contact_role": "unknown",
            "intent": "ask_whatsapp_channel",
            "objection": "none",
            "interests": ["whatsapp_interest"],
            "risk_level": "low",
            "human_review_required": False,
            "evidence": matches,
            "next_step": "present_short_proposal",
            "sales_agent_brief": "El lead pregunta por WhatsApp. Conviene explicar brevemente cómo entra WhatsApp en la propuesta, sin inventar integraciones.",
            "suggested_reply": "Sí, podemos pensarlo conectado a WhatsApp como canal de contacto. Primero te muestro la preview y vemos si aplica a tu local.",
            "crm_payload": {
                "commercial_state": "interested",
                "role": "unknown",
                "tags": ["whatsapp_interest"],
                "note": "Lead preguntó por WhatsApp como canal.",
            },
        }


    # Detecta interés en mostrar menú, carta o productos.
    matches = find_matches(message, MENU_QUESTION_KEYWORDS)
    if matches:
        return {
            "message_type": "menu_question",
            "tone": "curious",
            "sentiment": "neutral",
            "lead_state_suggestion": "interested",
            "contact_role": "unknown",
            "intent": "ask_menu_or_catalog",
            "objection": "none",
            "interests": ["menu_interest"],
            "risk_level": "low",
            "human_review_required": False,
            "evidence": matches,
            "next_step": "present_short_proposal",
            "sales_agent_brief": "El lead pregunta por menú o carta. Conviene explicar que la propuesta puede ordenar esa información, sin prometer funciones que no existen.",
            "suggested_reply": "Sí, la idea es que la carta o información clave del local quede más clara para quien los encuentra online.",
            "crm_payload": {
                "commercial_state": "interested",
                "role": "unknown",
                "tags": ["menu_interest"],
                "note": "Lead preguntó por menú o carta.",
            },
        }


    # Detecta interés en reservas o turnos.
    matches = find_matches(message, RESERVATION_QUESTION_KEYWORDS)
    if matches:
        return {
            "message_type": "reservation_question",
            "tone": "curious",
            "sentiment": "neutral",
            "lead_state_suggestion": "interested",
            "contact_role": "unknown",
            "intent": "ask_reservations",
            "objection": "none",
            "interests": ["reservations_interest"],
            "risk_level": "low",
            "human_review_required": False,
            "evidence": matches,
            "next_step": "present_short_proposal",
            "sales_agent_brief": "El lead pregunta por reservas. Conviene explicar con cuidado y no prometer backend ni sistema de reservas si no existe.",
            "suggested_reply": "Podemos mostrar la información de reservas o el canal de contacto. Si hace falta sistema real, eso habría que revisarlo aparte.",
            "crm_payload": {
                "commercial_state": "interested",
                "role": "unknown",
                "tags": ["reservations_interest"],
                "note": "Lead preguntó por reservas.",
            },
        }


    # Detecta objeciones como precio, falta de tiempo o “ya tengo web/Instagram”.
    matches = find_matches(message, OBJECTION_KEYWORDS)
    if matches:
        objection_detail = detect_objection_detail(message)
        return {
            "message_type": "objection",
            "tone": objection_detail["tone"],
            "sentiment": objection_detail["sentiment"],
            "lead_state_suggestion": "with_objection",
            "contact_role": "unknown",
            "intent": "raise_objection",
            "objection": objection_detail["objection"],
            "interests": objection_detail["interests"],
            "risk_level": "medium",
            "human_review_required": False,
            "evidence": matches,
            "next_step": objection_detail["next_step"],
            "sales_agent_brief": objection_detail["sales_agent_brief"],
            "suggested_reply": objection_detail["suggested_reply"],
            "crm_payload": {
                "commercial_state": "with_objection",
                "role": "unknown",
                "tags": objection_detail["tags"],
                "note": objection_detail["note"],
            },
        }


    #Pregunta quien sos
    matches = find_matches(message, WHO_ARE_YOU_KEYWORDS)
    if matches:
        return {
            "message_type": "who_are_you",
            "tone": "distrustful",
            "sentiment": "neutral",
            "lead_state_suggestion": "new",
            "contact_role": "unknown",
            "intent": "ask_identity",
            "objection": "spam_distrust",
            "interests": [],
            "risk_level": "medium",
            "human_review_required": False,
            "evidence": matches,
            "next_step": "explain_montserrat",
            "sales_agent_brief": "El lead quiere saber quién le escribe. Responder claro, breve y sin vender agresivamente.",
            "suggested_reply": "Soy de Montserrat. Te escribimos porque vimos el local y estamos preparando una preview simple para mostrar cómo podría verse mejor online.",
            "crm_payload": {
                "commercial_state": "new",
                "role": "unknown",
                "tags": ["identity_question", "possible_distrust"],
                "note": "Lead preguntó quién escribe o qué es la propuesta.",
            },
        }


    #Pregunta precio
    matches = find_matches(message, PRICING_KEYWORDS)
    if matches:
        return {
            "message_type": "pricing_question",
            "tone": "curious",
            "sentiment": "neutral",
            "lead_state_suggestion": "interested",
            "contact_role": "unknown",
            "intent": "ask_price",
            "objection": "none",
            "interests": ["pricing_question"],
            "risk_level": "low",
            "human_review_required": False,
            "evidence": matches,
            "next_step": "offer_demo_or_preview",
            "sales_agent_brief": "El lead pregunta precio. No inventar precio si no está disponible. Conviene llevar a preview o validar responsable.",
            "suggested_reply": "Te cuento corto. Primero podés ver la preview y ahí vemos si tiene sentido para tu local. ¿Sos quien maneja estos temas?",
            "crm_payload": {
                "commercial_state": "interested",
                "role": "unknown",
                "tags": ["pricing_question"],
                "note": "Lead preguntó por precio.",
            },
        }


    #Pide Demo o Link
    matches = find_matches(message, DEMO_KEYWORDS)
    if matches:
        return {
            "message_type": "demo_request",
            "tone": "interested",
            "sentiment": "positive",
            "lead_state_suggestion": "demo_requested",
            "contact_role": "unknown",
            "intent": "request_demo",
            "objection": "none",
            "interests": ["demo_interest"],
            "risk_level": "low",
            "human_review_required": False,
            "evidence": matches,
            "next_step": "offer_demo_or_preview",
            "sales_agent_brief": "El lead quiere ver una demo o preview. Conviene responder breve y avanzar sin pedir demasiados datos.",
            "suggested_reply": "Sí, te paso la preview. Antes confirmame algo rápido: ¿sos quien maneja la parte online del local?",
            "crm_payload": {
                "commercial_state": "demo_requested",
                "role": "unknown",
                "tags": ["demo_interest"],
                "note": "Lead pidió demo, preview o link.",
            },
        }


    matches = find_matches(message, GREETING_KEYWORDS)
    if matches and len(message) <= 20:
        return {
            "message_type": "minimal_greeting",
            "tone": "neutral",
            "sentiment": "neutral",
            "lead_state_suggestion": "new",
            "contact_role": "unknown",
            "intent": "greet",
            "objection": "none",
            "interests": [],
            "risk_level": "low",
            "human_review_required": False,
            "evidence": matches,
            "next_step": "explain_montserrat",
            "sales_agent_brief": "El lead solo saludó. Conviene responder con contexto mínimo.",
            "suggested_reply": "Hola, gracias por responder. Te escribo de Montserrat por una propuesta simple para mejorar cómo se ve el local online.",
            "crm_payload": {
                "commercial_state": "new",
                "role": "unknown",
                "tags": ["minimal_greeting"],
                "note": "Lead respondió con saludo mínimo.",
            },
        }
    #Si ninguna regla aplicó, no devolvemos nada.
    return None


















