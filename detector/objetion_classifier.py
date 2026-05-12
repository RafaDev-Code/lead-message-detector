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
            "interests": ["price_objection"],
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
            "interests": ["already_has_instagram"],
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
            "interests": ["already_has_website"],
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
            "interests": ["already_has_google_maps"],
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
            "interests": [],
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
            "interests": [],
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
            "interests": [],
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
            "interests": [],
            "tags": ["does_not_understand_offer"],
            "note": "Lead no entiende claramente la propuesta.",
        }

    return {
        "objection": "does_not_understand_offer",
        "interests": [],
        "tags": ["commercial_objection"],
        "note": "Lead planteó una objeción comercial general.",
    }