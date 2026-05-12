# app.py
import json


from detector.analyzer import analyze_lead_message
from tests.fake_cases import FAKE_CASES


total_cases = len(FAKE_CASES)
passed_cases = 0


for case in FAKE_CASES:
    #Por cada elemento que haya dentro de FAKE_CASES,
    #guardalo temporalmente en una variable llamada case
    #y ejecutá el bloque de código de abajo.
    result = analyze_lead_message(
        conversation=case["conversation"],
        last_message=case["last_message"],
        current_state=case["current_state"],
        business_context=None,
    )

    message_type_ok = result["message_type"] == case["expected_message_type"]

    risk_level_ok = result["risk_level"] == case["expected_risk_level"]

    next_step_ok = result["next_step"] == case["expected_next_step"]


    expected_objection = case.get("expected_objection")
    if expected_objection is None:
        objection_ok = True
    else:
        objection_ok = result["objection"] == expected_objection


    expected_do_not_do_contains = case.get("expected_do_not_do_contains", [])
    do_not_do_ok = True
    do_not_do_errors = []

    for expected_item in expected_do_not_do_contains:
        if expected_item not in result["do_not_do"]:
            do_not_do_ok = False
            do_not_do_errors.append(
                f"faltó '{expected_item}' en do_not_do"
            )


    expected_extracted_data = case.get("expected_extracted_data", {})
    extracted_data_ok = True
    extracted_data_errors = []

    for field_name, expected_value in expected_extracted_data.items():
        obtained_value = result["extracted_data"].get(field_name)
        if obtained_value != expected_value:
            extracted_data_ok = False
            extracted_data_errors.append(
                f"{field_name}: esperado: {expected_value} obtained: {obtained_value}"
            )


    case_passed = (
            message_type_ok
            and risk_level_ok
            and next_step_ok
            and objection_ok
            and extracted_data_ok
            and do_not_do_ok
    )

    if case_passed:
        passed_cases += 1

    print("\n" + "=" * 60)
    print(f"CASO: {case['name']}")
    print(f"MENSAJE: {case['last_message']}")

    if case_passed:
        print("RESULTADO: PASO WOW")

    else:
        print("RESULTADO: NO PASO MEN")

    print("-" * 60)
    print(f"message_type esperado: {case['expected_message_type']}")
    print(f"message_type obtenido: {result['message_type']}")

    print(f"risk_level esperado: {case['expected_risk_level']}")
    print(f"riks_level obetenido: {result['risk_level']}")

    print(f"next_step esperado: {case['expected_next_step']}")
    print(f"next_step obtenido: {result['next_step']}")
    print("-" * 60)

    if expected_objection is not None:
        print(f"objection esperado:    {expected_objection}")
        print(f"objection obtenido:     {result['objection']}")

    if expected_extracted_data:
        print("-" * 60)
        print("EXTRACTED DATA CHECK")
        if extracted_data_ok:
            print("EXTRACTED DATA OK")
        else:
            print("EXTRACTED DATA ERROR")
            for error in extracted_data_errors:
                print(f"- {error}")

    print("-" * 60)

    if expected_do_not_do_contains:
        print("-" * 60)
        print("DO NOT DO CHECK")
        if do_not_do_ok:
            print("do_not_do: ✅ OK")
        else:
            print("do_not_do: ❌ FALLÓ")
            for error in do_not_do_errors:
                print(f"- {error}")
    print(json.dumps(result, indent=2, ensure_ascii=False))

print("\n" + "=" * 60)
print("RESUMEN FINAL")
print("=" * 60)
print(f"Casos totales: {total_cases}")
print(f"Casos OK: {passed_cases}")
print(f"Casos FALLIDOS: {total_cases - passed_cases}")