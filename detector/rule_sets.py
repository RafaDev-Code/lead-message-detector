# Este archivo guarda las listas de palabras/frases que activan reglas.
# Solo contiene datos reutilizables.


# Frases que indican que el lead no quiere recibir más mensajes.
OPT_OUT_KEYWORDS = [
    "no me escribas",
    "no me escriban",
    "no molesten",
    "no quiero que me contacten",
    "borrame",
    "sacame",
    "stop",
    "baja",
    "dar de baja",
]


# Frases que indican riesgo alto, agresión, amenaza o posible problema legal.
SENSITIVE_KEYWORDS = [
    "te voy a denunciar",
    "denuncia",
    "abogado",
    "legal",
    "estafa",
    "chantas",
    "ladrones",
    "hijos de puta",
    "andate a la mierda",
    "me están acosando",
    "me estan acosando",
]


# Frases que indican que el lead quiere hablar con una persona.
ASKS_HUMAN_KEYWORDS = [
    "quiero hablar con una persona",
    "quiero hablar con alguien",
    "pasame con alguien",
    "pasame con un humano",
    "me atiende una persona",
    "sos un bot",
    "no quiero hablar con un bot",
]


# Frases que indican soporte, error o problema técnico.
SUPPORT_KEYWORDS = [
    "no funciona",
    "tengo un problema",
    "necesito ayuda",
    "soporte",
    "no puedo entrar",
    "no me llegó",
    "no me llego",
    "error",
    "falló",
    "fallo",
]


# Frases que indican rechazo comercial simple.
REJECTION_KEYWORDS = [
    "no me interesa",
    "no nos interesa",
    "por ahora no",
    "no gracias",
    "gracias pero no",
    "no queremos",
    "no hace falta",
]


# Frases que indican número equivocado.
WRONG_NUMBER_KEYWORDS = [
    "número equivocado",
    "numero equivocado",
    "te equivocaste",
    "no es acá",
    "no es aca",
    "no conozco ese local",
    "no soy de ese negocio",
]


# Frases que indican que la persona no es dueña o no decide.
NOT_OWNER_KEYWORDS = [
    "no soy el dueño",
    "no soy dueño",
    "soy empleado",
    "soy empleada",
    "trabajo acá",
    "trabajo aca",
    "no manejo eso",
    "eso lo ve mi jefe",
    "hablá con el dueño",
    "habla con el dueño",
]


# Frases que indican que el lead pregunta quién escribe.
WHO_ARE_YOU_KEYWORDS = [
    "quién sos",
    "quien sos",
    "de dónde sos",
    "de donde sos",
    "quiénes son",
    "quienes son",
    "qué es esto",
    "que es esto",
]


# Frases que indican que la persona confirma que ese número sí pertenece al local.
CONFIRMS_BUSINESS_KEYWORDS = [
    "sí, es el local",
    "si, es el local",
    "sí somos",
    "si somos",
    "es acá",
    "es aca",
    "este es el local",
    "somos el local",
    "sí, correcto",
    "si, correcto",
]


# Frases que indican pregunta sobre WhatsApp como canal.
WHATSAPP_QUESTION_KEYWORDS = [
    "tienen whatsapp",
    "tenés whatsapp",
    "tenes whatsapp",
    "atienden por whatsapp",
    "se puede por whatsapp",
    "tienen wpp",
    "tenés wpp",
    "tenes wpp",
]


# Frases que indican pregunta por menú o carta.
MENU_QUESTION_KEYWORDS = [
    "tienen menú",
    "tienen menu",
    "tienen carta",
    "pasame la carta",
    "pasame el menú",
    "pasame el menu",
    "quiero ver la carta",
    "quiero ver el menú",
    "quiero ver el menu",
]


# Frases que indican pregunta por reservas.
RESERVATION_QUESTION_KEYWORDS = [
    "hacen reservas",
    "toman reservas",
    "se puede reservar",
    "puedo reservar",
    "tienen reservas",
    "quiero reservar",
    "reserva",
]


#Frases que indican objeciones.
OBJECTION_KEYWORDS = [
    "muy caro",
    "es caro",
    "no puedo pagar",
    "no tengo tiempo",
    "no tenemos tiempo",
    "ya tengo instagram",
    "ya tenemos instagram",
    "ya usamos instagram",
    "con instagram estamos",
    "ya tengo web",
    "ya tenemos web",
    "ya tengo página",
    "ya tengo pagina",
    "ya tenemos página",
    "ya tenemos pagina",
    "ya tenemos sitio",
    "ya tengo sitio",
    "ya tenemos google maps",
    "ya tengo google maps",
    "ya estamos en google",
    "ya aparecemos en google",
    "ya estamos en maps",
    "no entiendo",
    "qué sería",
    "que sería",
    "qué hacen",
    "que hacen",
    "qué datos necesitan",
    "que datos necesitan",
    "para qué quieren mis datos",
    "para que quieren mis datos",
    "no quiero pasar datos",
    "privacidad",
    "datos personales",
    "no quiero que publiquen cualquier cosa",
    "no quiero que suban cualquier cosa",
    "no publiquen sin permiso",
    "no suban nada sin permiso",
    "estoy ocupado",
    "estamos ocupados",
    "ahora no puedo",
    "no puedo verlo ahora",
]


# Frases que indican pregunta de precio.
PRICING_KEYWORDS = [
    "cuánto sale",
    "cuanto sale",
    "precio",
    "cuánto cuesta",
    "cuanto cuesta",
    "qué vale",
    "que vale",
    "tarifa",
    "costo",
]


# Frases que indican pedido de demo, preview o link.
DEMO_KEYWORDS = [
    "demo",
    "preview",
    "link",
    "quiero verlo",
    "me interesa verlo",
    "mostrame",
]


# Frases que indican saludo mínimo.
GREETING_KEYWORDS = [
    "hola",
    "buenas",
    "buen día",
    "buen dia",
    "buenas tardes",
    "buenas noches",
]
