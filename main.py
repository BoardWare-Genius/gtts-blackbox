from io import BytesIO

import uvicorn
from fastapi import FastAPI, Response
from gtts import gTTS
from pydantic import BaseModel


def processing(text: str) -> BytesIO:
    tts = gTTS(text=text, lang="en")
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp


app = FastAPI()


class Payload(BaseModel):
    text: str

@app.post("/")
async def root(prompt: Payload):
    try:
        return Response(content=processing(prompt.text).read(), media_type="audio/mp3", headers={"Content-Disposition": "attachment; filename=audio.mp3"})
    except Exception as e:
        return Response(content=str(e), media_type="text/plain", status_code=500)
        
@app.post("/{x}")
async def root_w(prompt: Payload):
    try:
        return Response(content=processing(prompt.text).read(), media_type="audio/mp3", headers={"Content-Disposition": "attachment; filename=audio.mp3"})
    except Exception as e:
        return Response(content=str(e), media_type="text/plain", status_code=500)

@app.post("/gtts-blackbox")
async def gtts_blackbox(prompt: Payload):
    try:
        return Response(content=processing(prompt.text).read(), media_type="audio/mp3", headers={"Content-Disposition": "attachment; filename=audio.mp3"})
    except Exception as e:
        return Response(content=str(e), media_type="text/plain", status_code=500)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
