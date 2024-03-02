from typing import Dict
from fastapi import Depends, FastAPI
from pydantic import BaseModel
import base64
from io import BytesIO

from generator.model import Model, get_model

class GenerativeRequest(BaseModel):
    prompt: str
    negative_prompt: str

class GenerativeResponse(BaseModel):
    base64: str


app = FastAPI()

@app.post("/generate")
def generate(request: GenerativeRequest, model: Model = Depends(get_model)):
    image = model.generate(request.prompt, request.negative_prompt)
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue())
    return GenerativeResponse(
      base64=img_str
    )
