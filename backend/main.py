from fastapi import FastAPI

app = FastAPI(title="ElderGuard AI Telemetry API")

@app.get("/")
def root():
    return {"status": "online", "system": "ElderGuard AI"}

@app.post("/api/v1/telemetry")
def receive_telemetry(data: dict):
    return {"message": "Telemetry received successfully", "data": data}