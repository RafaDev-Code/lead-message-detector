def build_do_not_do(analysis_result: dict) -> list[str]:
    do_not_do = []

    risk_level = analysis_result["risk_level"]
    next_step = analysis_result["next_step"]
    message_type = analysis_result["message_type"]

    do_not_do.append("no_inventar_precio")

    do_not_do.append("no_prometar_resultados")

    if risk_level == "high":
        do_not_do.append("no_vender")

    if next_step == "register_opt_out":
        do_not_do.append("no_insistir")
        do_not_do.append("no_volver_a_contactar")
        do_not_do.append("registrar_opt_out")

    if next_step == "send_to_human":
        do_not_do.append("no_seguir_automatizando")
        do_not_do.append("derivar_a_humano")

    if message_type == "asks_human":
        do_not_do.append("no_evitar_derivacion_humana")

    if message_type == "rejection":
        do_not_do.append("no_presionar")

    if message_type == "objection":
        do_not_do.append("no_discutir")
        do_not_do.append("no_minimizar_objecion")

    if message_type == "pricing_question":
        do_not_do.append("no_dar_precio_si_no_esta_disponible")

    return do_not_do