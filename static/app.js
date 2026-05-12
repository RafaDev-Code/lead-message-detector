const chatBox = document.getElementById("chatBox");
const demoList = document.getElementById("demoList");
const messageType = document.getElementById("messageType");
const riskLevel = document.getElementById("riskLevel");
const nextStep = document.getElementById("nextStep");
const salesBrief = document.getElementById("salesBrief");
const doNotDoList = document.getElementById("doNotDoList");
const jsonOutput = document.getElementById("jsonOutput");

let isAnalyzing = false;


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


const RISK_LABELS = {
    low: "Bajo",
    medium: "Medio",
    high: "Alto",
};


function getMetricCard(element) {
    return element.parentElement;
}


function formatCodeValue(value) {
    return value.replaceAll("_", " ");
}


function setMetricValue(element, value, formatter = formatCodeValue) {
    element.textContent = formatter(value);
    element.title = value;
}


function formatDoNotDo(item) {
    return DO_NOT_DO_LABELS[item] || item.replaceAll("_", " ");
}


function escapeHtml(value) {
    return value.replace(/[&<>"']/g, (character) => {
        const replacements = {
            "&": "&amp;",
            "<": "&lt;",
            ">": "&gt;",
            "\"": "&quot;",
            "'": "&#039;",
        };

        return replacements[character];
    });
}


function renderJson(value) {
    const json = JSON.stringify(value, null, 2);

    jsonOutput.innerHTML = json.replace(
        /("(\\u[\da-fA-F]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+-]?\d+)?)/g,
        (match) => {
            let tokenClass = "json-number";

            if (match.startsWith("\"")) {
                tokenClass = match.endsWith(":") ? "json-key" : "json-string";
            } else if (match === "true" || match === "false") {
                tokenClass = "json-boolean";
            } else if (match === "null") {
                tokenClass = "json-null";
            }

            return `<span class="${tokenClass}">${escapeHtml(match)}</span>`;
        }
    );
}


function setAnalyzingState(isLoading) {
    document.body.classList.toggle("is-analyzing", isLoading);

    document.querySelectorAll(".demo-button").forEach((button) => {
        button.disabled = isLoading;
    });

    if (!isLoading) {
        return;
    }

    messageType.textContent = "analizando";
    riskLevel.textContent = "analizando";
    nextStep.textContent = "analizando";
    salesBrief.textContent = "Analizando el mensaje del lead...";
    doNotDoList.innerHTML = "";

    getMetricCard(messageType).dataset.state = "loading";
    getMetricCard(riskLevel).dataset.state = "loading";
    getMetricCard(riskLevel).dataset.risk = "analyzing";
    getMetricCard(nextStep).dataset.state = "loading";

    renderJson({
        status: "analizando",
    });
}


function addMessage(text, type) {
    const message = document.createElement("div");
    message.className = `message ${type}`;
    message.textContent = text;

    chatBox.appendChild(message);
    chatBox.scrollTop = chatBox.scrollHeight;

    return message;
}


function renderAnalysis(result) {
    getMetricCard(messageType).dataset.state = "ready";
    getMetricCard(riskLevel).dataset.state = "ready";
    getMetricCard(riskLevel).dataset.risk = result.risk_level;
    getMetricCard(nextStep).dataset.state = "ready";

    setMetricValue(messageType, result.message_type);
    setMetricValue(riskLevel, result.risk_level, (value) => RISK_LABELS[value] || value);
    setMetricValue(nextStep, result.next_step);
    salesBrief.textContent = result.sales_agent_brief;
    doNotDoList.innerHTML = "";

    result.do_not_do.forEach((item) => {
        const li = document.createElement("li");
        li.textContent = formatDoNotDo(item);
        doNotDoList.appendChild(li);
    });

    renderJson(result);
}


async function runDemo(demo) {
    if (isAnalyzing) {
        return;
    }

    isAnalyzing = true;
    setAnalyzingState(true);

    addMessage(demo.last_message, "lead");
    const analyzingMessage = addMessage("Analizando", "system analyzing");

    try {
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

        if (!response.ok) {
            throw new Error("No se pudo analizar el mensaje.");
        }

        const result = await response.json();

        analyzingMessage.remove();
        addMessage(result.suggested_reply, "agent");

        renderAnalysis(result);
    } catch (error) {
        getMetricCard(messageType).dataset.state = "error";
        getMetricCard(riskLevel).dataset.state = "error";
        getMetricCard(riskLevel).dataset.risk = "error";
        getMetricCard(nextStep).dataset.state = "error";

        messageType.textContent = "error";
        riskLevel.textContent = "error";
        nextStep.textContent = "reintentar";
        analyzingMessage.className = "message system error";
        analyzingMessage.textContent = "No se pudo analizar el mensaje.";
        salesBrief.textContent = "Hubo un error al analizar el mensaje. Probá de nuevo.";
        renderJson({
            error: error.message,
        });
    } finally {
        setAnalyzingState(false);
        isAnalyzing = false;
    }
}


async function loadDemoCases() {
    const response = await fetch("/demo-cases");

    const categories = await response.json();

    Object.entries(categories).forEach(([categoryName, demos], categoryIndex) => {
        const details = document.createElement("details");
        details.open = categoryIndex === 0;
        details.className = "demo-category";

        const summary = document.createElement("summary");
        const summaryTitle = document.createElement("span");
        const summaryCount = document.createElement("span");

        summaryTitle.textContent = categoryName;
        summaryCount.className = "demo-count";
        summaryCount.textContent = demos.length;

        summary.appendChild(summaryTitle);
        summary.appendChild(summaryCount);
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
