def build_do_not_do(analysis_result: dict) -> list[str]:
    do_not_do = []

    risk_level = analysis_result["risk_level"]
    next_step = analysis_result["next_step"]
    message_type = analysis_result["message_type"]
    objection = analysis_result["objection"]

    do_not_do.append("no_inventar_precio")

    do_not_do.append("no_prometer_resultados")

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

    if objection == "price":
        do_not_do.append("no_dar_precio_sin_preview")
        do_not_do.append("no_ofrecer_descuento_sin_contexto")

    if objection == "already_has_website":
        do_not_do.append("no_reemplazar_web")
        do_not_do.append("no_descalificar_web_actual")

    if objection == "already_has_instagram":
        do_not_do.append("no_reemplazar_instagram")
        do_not_do.append("no_descalificar_canal_actual")

    if objection == "already_has_google_maps":
        do_not_do.append("no_competir_con_google_maps")
        do_not_do.append("no_descalificar_canal_actual")

    if objection == "no_time":
        do_not_do.append("no_mandar_mensaje_largo")
        do_not_do.append("no_pedir_reunion_ahora")

    if objection == "privacy_data":
        do_not_do.append("no_pedir_datos_de_mas")
        do_not_do.append("no_usar_datos_sin_explicar")

    if objection == "fear_wrong_publication":
        do_not_do.append("no_publicar_sin_validacion")
        do_not_do.append("no_minimizar_miedo_a_error")

    if objection == "does_not_understand_offer":
        do_not_do.append("no_usar_tecnicismos")
        do_not_do.append("no_pedir_datos_todavia")

    if message_type == "pricing_question":
        do_not_do.append("no_dar_precio_si_no_esta_disponible")

    return do_not_do
