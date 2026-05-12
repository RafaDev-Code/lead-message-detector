from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from detector.analyzer import analyze_lead_message
from detector.demo_cases import DEMO_CATEGORIES

app = FastAPI(
    tittle="Lead Message Detector",
    description="API + demo visual para analizar mensajes de leads antes del Sales Agent.",
    version="0.1.0",
)

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

class LeadMessageRequest(BaseModel):
    conversation: str
    last_message: str
    current_state: str | None = None
    business_context: str | None = None

@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "lead-message-detector",
        "version": "0.1.0",
    }
@app.get("/demo-cases")
def get_demo_cases():

    # Devolvemos el diccionario de demos.
    return DEMO_CATEGORIES


@app.post("/analyze")
def analyze_lead(request: LeadMessageRequest):
    result = analyze_lead_message(
        conversation=request.conversation,
        last_message=request.last_message,
        current_state=request.current_state,
        business_context=request.business_context
    )

    return result