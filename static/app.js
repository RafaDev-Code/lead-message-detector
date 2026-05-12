const chatBox = document.getElementById("chatBox");
const demoList = document.getElementById("demoList");
const messageType = document.getElementById("messageType");
const riskLevel = document.getElementById("riskLevel");
const nextStep = document.getElementById("nextStep");
const salesBrief = document.getElementById("salesBrief");
const doNotDoList = document.getElementById("doNotDoList");
const jsonOutput = document.getElementById("jsonOutput");


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
        li.textContent = item;
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