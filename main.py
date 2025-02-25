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
    return Response(content=processing(prompt.text).read(), media_type="audio/mp3", headers={"Content-Disposition": "attachment; filename=audio.mp3"})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
