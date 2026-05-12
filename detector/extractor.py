import re

def extract_mentioned_channels(message: str) -> list[str]:
    channels = []

    if "whatsapp" in message or "wpp" in message:
        channels.append("whatsapp")

    if "instagram" in message or "insta" in message:
        channels.append("instagram")

    if "google" in message or "maps" in message:
        channels.append("google")

    if "web" in message or "página" in message or "pagina" in message or "sitio" in message:
        channels.append("web")

    return channels


def extract_request_features(message: str) -> list[str]:
    features = []

    if "menu" in message or "menú" in message or "carta" in message:
        features.append("menu")

    if "reserva" in message or "reservas" in message:
        features.append("reservations")

    if "horario" in message or "horarios" in message:
        features.append("hours")

    if "foto" in message or "fotos" in message or "imagen" in message or "imágenes" in message:
        features.append("photos")

    if "contacto" in message or "teléfono" in message or "telefono" in message:
        features.append("contact")

    if "demo" in message or "preview" in message or "link" in message:
        features.append("demo")

    return features


def extract_followup_window(message: str) -> str | None:

    if "mañana" in message or "manana" in message:
        return "mañana"

    if "más tarde" in message or "mas tarde" in message:
        return "más tarde"

    if "semana que viene" in message or "la semana que viene" in message:
        return "semana que viene"

    return None


def extract_phone_or_whatsapp(message: str) -> str | None:

    phone_match = re.search(r"(\+?\d[\d\s\-]{6,}\d)", message)

    if phone_match:
        return phone_match.group(0).strip()
    return None


def extract_data(message: str) -> dict:
    return {
        "business_name": None,
        "person_name": None,
        "role_declared": None,
        "phone_or_whatsapp": extract_phone_or_whatsapp(message),
        "mentioned_channels": extract_mentioned_channels(message),
        "requested_features": extract_request_features(message),
        "followup_window": extract_followup_window(message),
    }