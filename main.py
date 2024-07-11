from fastapi import FastAPI, Request
import gemini
import asyncio
import base64
app = FastAPI()


@app.get("/")
async def confirm(request: Request):
    return "Your server is working!"
    
@app.post("/image/")
async def read_image(request: Request):
    request = await request.json()
    with open("question.png", "wb") as image:
        image.write(base64.b64decode(request['image'].replace('data:image/png;base64,','')))
        
    return gemini.text_in_image(request['key'], request['prompt'], "question.png", request['model_name'])

@app.post("/text/")
async def read_text(request: Request):
    
    return gemini.text_only(request['key'], request['prompt'], request['model_name'])


