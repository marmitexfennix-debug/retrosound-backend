from fastapi import FastAPI
import uuid

from certificate import generate_certificate

app = FastAPI()

@app.get("/")
def home():
    return {"msg": "API RetroSound funcionando"}

@app.post("/generate")
def generate(prompt: str):

    music_id = str(uuid.uuid4())

    preview = f"/audio/{music_id}_preview.mp3"
    full = f"/audio/{music_id}_full.mp3"

    cert = generate_certificate("user", music_id)

    return {
        "preview": preview,
        "full": full,
        "locked": True,
        "certificate": cert
    }
