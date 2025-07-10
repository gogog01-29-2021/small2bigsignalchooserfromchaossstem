from fastapi import FastAPI, WebSocket

from .router import route_query

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "small2big_chat"}


@app.post("/chat")
async def chat_endpoint(q: str):
    reply, meta = await route_query(q)
    return {"reply": reply, "meta": meta}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            reply, meta = await route_query(data)
            await websocket.send_json({"reply": reply, "meta": meta})
    except Exception:
        await websocket.close()
