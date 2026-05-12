def contains_any(message: str, keywords: list[str]) -> bool:

    for keyword in keywords:

        if keyword in message:
            return True
    return False


def detect_objection_detail(message: str) -> dict:


    price_keywords = [
        "muy caro",
        "es caro",
        "carísimo",
        "carisimo",
        "no puedo pagar",
        "no podemos pagar",
        "se me va de presupuesto",
    ]

    if contains_any(message, price_keywords):
        return {
            "objection": "price",
            "tone": "distrustful",
            "sentiment": "mixed",
            "interests": ["price_objection"],
            "next_step": "offer_demo_or_preview",
            "sales_agent_brief": "El lead objeta precio. No inventar precio ni defender el costo de entrada. Primero mostrar la preview para que vea valor concreto.",
            "suggested_reply": "Entiendo. Para no hablar de precio en abstracto, primero te muestro la preview y ves si tiene sentido para el local.",
            "tags": ["price_objection"],
            "note": "Lead planteó objeción de precio.",
        }



    instagram_keywords = [
        "ya tengo instagram",
        "ya tenemos instagram",
        "ya usamos instagram",
        "con instagram estamos",
    ]

    if contains_any(message, instagram_keywords):
        return {
            "objection": "already_has_instagram",
            "tone": "neutral",
            "sentiment": "mixed",
            "interests": ["already_has_instagram"],
            "next_step": "present_short_proposal",
            "sales_agent_brief": "El lead ya usa Instagram. No plantear reemplazo. Mostrar una mejora puntual para ordenar la información fuera del feed.",
            "suggested_reply": "Perfecto, Instagram suma. La idea no es reemplazarlo, sino mostrar una mejora puntual para que la info clave del local quede más clara.",
            "tags": ["already_has_instagram"],
            "note": "Lead indicó que ya usa Instagram.",
        }


    website_keywords = [
        "ya tengo web",
        "ya tenemos web",
        "ya tengo página",
        "ya tengo pagina",
        "ya tenemos página",
        "ya tenemos pagina",
        "ya tenemos sitio",
        "ya tengo sitio",
    ]

    if contains_any(message, website_keywords):
        return {
            "objection": "already_has_website",
            "tone": "neutral",
            "sentiment": "mixed",
            "interests": ["already_has_website"],
            "next_step": "present_short_proposal",
            "sales_agent_brief": "El lead ya tiene web. No decir que hay que reemplazarla. Mostrar una mejora puntual o una preview complementaria.",
            "suggested_reply": "Buenísimo. No hace falta reemplazar la web. Te muestro una mejora puntual y vemos si complementa lo que ya tienen.",
            "tags": ["already_has_website"],
            "note": "Lead indicó que ya tiene web o página.",
        }


    google_maps_keywords = [
        "ya tengo google maps",
        "ya tenemos google maps",
        "ya estamos en google",
        "ya aparecemos en google",
        "ya estamos en maps",
    ]

    if contains_any(message, google_maps_keywords):
        return {
            "objection": "already_has_google_maps",
            "tone": "neutral",
            "sentiment": "mixed",
            "interests": ["already_has_google_maps"],
            "next_step": "present_short_proposal",
            "sales_agent_brief": "El lead ya aparece en Google Maps. No competir con Maps. Mostrar cómo la preview puede ordenar o reforzar la información pública.",
            "suggested_reply": "Perfecto, Google Maps ya les da visibilidad. La preview sería para ordenar mejor la información que ve el cliente antes de escribirles.",
            "tags": ["already_has_google_maps"],
            "note": "Lead indicó que ya tiene presencia en Google Maps.",
        }


    no_time_keywords = [
        "no tengo tiempo",
        "no tenemos tiempo",
        "estoy ocupado",
        "estamos ocupados",
        "ahora no puedo",
        "no puedo verlo ahora",
    ]

    if contains_any(message, no_time_keywords):
        return {
            "objection": "no_time",
            "tone": "rushed",
            "sentiment": "neutral",
            "interests": [],
            "next_step": "schedule_followup",
            "sales_agent_brief": "El lead no tiene tiempo. Responder muy corto, no explicar toda la propuesta y sugerir seguimiento simple.",
            "suggested_reply": "Cero problema. Te dejo algo corto para mirar cuando puedas y lo retomamos más tarde si te sirve.",
            "tags": ["no_time"],
            "note": "Lead indicó falta de tiempo.",
        }


    privacy_keywords = [
        "qué datos necesitan",
        "que datos necesitan",
        "para qué quieren mis datos",
        "para que quieren mis datos",
        "no quiero pasar datos",
        "privacidad",
        "datos personales",
    ]

    if contains_any(message, privacy_keywords):
        return {
            "objection": "privacy_data",
            "tone": "distrustful",
            "sentiment": "mixed",
            "interests": [],
            "next_step": "ask_minimum_data",
            "sales_agent_brief": "El lead pregunta por datos o privacidad. Pedir solo lo mínimo y explicar para qué se usa cada dato.",
            "suggested_reply": "Tiene sentido preguntar. Solo pediríamos lo mínimo para armar la preview y no publicamos nada sin validarlo.",
            "tags": ["privacy_data_objection"],
            "note": "Lead mostró preocupación por datos o privacidad.",
        }


    wrong_publication_keywords = [
        "no quiero que publiquen cualquier cosa",
        "no quiero que suban cualquier cosa",
        "no publiquen sin permiso",
        "no suban nada sin permiso",
    ]

    if contains_any(message, wrong_publication_keywords):
        return {
            "objection": "fear_wrong_publication",
            "tone": "distrustful",
            "sentiment": "mixed",
            "interests": [],
            "next_step": "present_short_proposal",
            "sales_agent_brief": "El lead teme que se publique algo incorrecto. Aclarar que no se publica nada sin validación y mostrar preview primero.",
            "suggested_reply": "Tranqui, no publicaríamos nada sin validarlo con ustedes. Primero sería una preview para revisar si está bien.",
            "tags": ["fear_wrong_publication"],
            "note": "Lead mostró miedo a que se publique algo incorrecto.",
        }


    does_not_understand_keywords = [
        "no entiendo",
        "no entiendo para qué",
        "no entiendo para que",
        "qué sería",
        "que sería",
        "qué hacen",
        "que hacen",
    ]

    if contains_any(message, does_not_understand_keywords):
        return {
            "objection": "does_not_understand_offer",
            "tone": "confused",
            "sentiment": "neutral",
            "interests": [],
            "next_step": "explain_montserrat",
            "sales_agent_brief": "El lead no entiende la propuesta. Explicar en una frase, sin tecnicismos y sin pedir datos todavía.",
            "suggested_reply": "Te explico simple: preparamos una preview de cómo podría verse mejor la información del local online, y después ves si te sirve.",
            "tags": ["does_not_understand_offer"],
            "note": "Lead no entiende claramente la propuesta.",
        }

    return {
        "objection": "does_not_understand_offer",
        "tone": "distrustful",
        "sentiment": "mixed",
        "interests": [],
        "next_step": "answer_objection",
        "sales_agent_brief": "El lead planteó una objeción comercial general. Responder breve, reconocer la duda y no presionar.",
        "suggested_reply": "Tiene sentido. Te lo muestro corto con una preview y, si no suma, no avanzamos.",
        "tags": ["commercial_objection"],
        "note": "Lead planteó una objeción comercial general.",
    }
