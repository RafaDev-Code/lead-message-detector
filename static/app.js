const chatBox = document.getElementById("chatBox");
const demoList = document.getElementById("demoList");
const messageType = document.getElementById("messageType");
const riskLevel = document.getElementById("riskLevel");
const nextStep = document.getElementById("nextStep");
const salesBrief = document.getElementById("salesBrief");
const doNotDoList = document.getElementById("doNotDoList");
const jsonOutput = document.getElementById("jsonOutput");


const DO_NOT_DO_LABELS = {
    no_inventar_precio: "No inventar precio",
    no_prometer_resultados: "No prometer resultados",
    no_vender: "No vender",
    no_insistir: "No insistir",
    no_volver_a_contactar: "No volver a contactar",
    registrar_opt_out: "Registrar opt-out",
    no_seguir_automatizando: "No seguir automatizando",
    derivar_a_humano: "Derivar a humano",
    no_evitar_derivacion_humana: "No evitar derivación humana",
    no_presionar: "No presionar",
    no_discutir: "No discutir",
    no_minimizar_objecion: "No minimizar la objeción",
    no_dar_precio_si_no_esta_disponible: "No dar precio si no está disponible",
    no_dar_precio_sin_preview: "No dar precio sin mostrar preview",
    no_ofrecer_descuento_sin_contexto: "No ofrecer descuento sin contexto",
    no_reemplazar_web: "No plantear reemplazo de web",
    no_descalificar_web_actual: "No descalificar la web actual",
    no_reemplazar_instagram: "No plantear reemplazo de Instagram",
    no_descalificar_canal_actual: "No descalificar el canal actual",
    no_competir_con_google_maps: "No competir contra Google Maps",
    no_mandar_mensaje_largo: "No mandar mensaje largo",
    no_pedir_reunion_ahora: "No pedir reunión ahora",
    no_pedir_datos_de_mas: "No pedir datos de más",
    no_usar_datos_sin_explicar: "No usar datos sin explicar",
    no_publicar_sin_validacion: "No publicar sin validación",
    no_minimizar_miedo_a_error: "No minimizar el miedo a errores",
    no_usar_tecnicismos: "No usar tecnicismos",
    no_pedir_datos_todavia: "No pedir datos todavía",
};


function formatDoNotDo(item) {
    return DO_NOT_DO_LABELS[item] || item.replaceAll("_", " ");
}


function addMessage(text, type) {
    const message = document.createElement("div");
    message.className = `message ${type}`;
    message.textContent = text;

    chatBox.appendChild(message);
    chatBox.scrollTop = chatBox.scrollHeight;
}


function renderAnalysis(result) {
    messageType.textContent = result.message_type;
    riskLevel.textContent = result.risk_level;
    nextStep.textContent = result.next_step;
    salesBrief.textContent = result.sales_agent_brief;
    doNotDoList.innerHTML = "";

    result.do_not_do.forEach((item) => {
        const li = document.createElement("li");
        li.textContent = formatDoNotDo(item);
        doNotDoList.appendChild(li);
    });

    jsonOutput.textContent = JSON.stringify(result, null, 2);
}


async function runDemo(demo) {
    addMessage(demo.last_message, "lead");
    const response = await fetch("/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },

        body: JSON.stringify({
            conversation: demo.conversation,
            last_message: demo.last_message,
            current_state: demo.current_state,
            business_context: null,
        }),
    });

    const result = await response.json();

    addMessage(result.suggested_reply, "agent");

    renderAnalysis(result);
}


async function loadDemoCases() {
    const response = await fetch("/demo-cases");

    const categories = await response.json();

    Object.entries(categories).forEach(([categoryName, demos]) => {
        const details = document.createElement("details");
        details.open = true;
        details.className = "demo-category";

        const summary = document.createElement("summary");

        summary.textContent = categoryName;

        details.appendChild(summary);

        const buttonsContainer = document.createElement("div");

        buttonsContainer.className = "demo-buttons";

        demos.forEach((demo) => {
            const button = document.createElement("button");
            button.className = "demo-button";

            button.textContent = demo.title;
            button.addEventListener("click", () => runDemo(demo));
            buttonsContainer.appendChild(button);
        });

        details.appendChild(buttonsContainer);

        demoList.appendChild(details);
    });
}


loadDemoCases();
