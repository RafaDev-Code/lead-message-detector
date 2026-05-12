DEMO_CATEGORIES = {
    # Categoría de consultas comerciales.
    "Comercial": [
        {
            "title": "Pregunta precio",
            "conversation": "",
            "last_message": "cuánto sale?",
            "current_state": "new",
        },
        {
            "title": "Pide demo/link",
            "conversation": "",
            "last_message": "pasame el link por wpp, quiero ver la carta mañana",
            "current_state": "new",
        },
        {
            "title": "Pregunta por menú",
            "conversation": "",
            "last_message": "tienen menú para ver?",
            "current_state": "new",
        },
        {
            "title": "Pregunta por reservas",
            "conversation": "",
            "last_message": "se puede reservar?",
            "current_state": "new",
        },
    ],

    # Categoría de validaciones iniciales.
    "Validación": [
        {
            "title": "Confirma que es el local",
            "conversation": "",
            "last_message": "sí, es el local",
            "current_state": "number_validation_pending",
        },
        {
            "title": "No es dueño",
            "conversation": "",
            "last_message": "no soy el dueño, soy empleado",
            "current_state": "number_validated",
        },
        {
            "title": "Número equivocado",
            "conversation": "",
            "last_message": "te equivocaste, este no es el local",
            "current_state": "new",
        },
    ],

    # Categoría de objeciones.
    "Objeciones": [
        {
            "title": "Ya tiene web",
            "conversation": "",
            "last_message": "ya tenemos web, no entiendo para qué sería",
            "current_state": "new",
        },
        {
            "title": "Precio caro",
            "conversation": "",
            "last_message": "me parece muy caro",
            "current_state": "new",
        },
        {
            "title": "Falta de tiempo",
            "conversation": "",
            "last_message": "ahora no puedo, no tengo tiempo",
            "current_state": "new",
        },
    ],

    # Categoría de riesgo.
    "Riesgo / No vender": [
        {
            "title": "Opt-out",
            "conversation": "",
            "last_message": "no me escribas más",
            "current_state": "new",
        },
        {
            "title": "Pide humano",
            "conversation": "",
            "last_message": "quiero hablar con una persona",
            "current_state": "new",
        },
        {
            "title": "Soporte",
            "conversation": "",
            "last_message": "tengo un problema, no funciona",
            "current_state": "new",
        },
        {
            "title": "Agresivo / estafa",
            "conversation": "",
            "last_message": "esto es una estafa, los voy a denunciar",
            "current_state": "new",
        },
    ],
}