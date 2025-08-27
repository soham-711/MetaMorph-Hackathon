# server.py
import asyncio
import threading
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from core.assistant import PicoAssistant

app = FastAPI()


class WSManager:
    def __init__(self):
        self.active_connections: set[WebSocket] = set()
        self.loop: asyncio.AbstractEventLoop | None = None

    def set_loop(self, loop: asyncio.AbstractEventLoop):
        self.loop = loop

    async def connect(self, websocket: WebSocket):
        # Accept and keep the connection. We wait for client messages
        await websocket.accept()
        self.active_connections.add(websocket)
        try:
            while True:
                # keep the connection alive; clients don't need to send anything
                await websocket.receive_text()
        except WebSocketDisconnect:
            self.active_connections.discard(websocket)
        except Exception:
            self.active_connections.discard(websocket)

    async def broadcast(self, message: dict):
        to_remove = []
        for ws in list(self.active_connections):
            try:
                await ws.send_json(message)
            except Exception:
                to_remove.append(ws)
        for ws in to_remove:
            self.active_connections.discard(ws)

    def publish_state(self, state: str):
        """Called from sync/background threads. Schedules an async broadcast."""
        if not self.loop:
            try:
                self.loop = asyncio.get_running_loop()
            except RuntimeError:
                return
        # schedule the broadcast coroutine on the event loop
        self.loop.call_soon_threadsafe(asyncio.create_task, self.broadcast({"event": "state", "value": state}))


ws_manager = WSManager()
assistant: PicoAssistant | None = None


@app.on_event("startup")
async def startup_event():
    # capture server event loop for thread-safe publishing
    ws_manager.set_loop(asyncio.get_running_loop())

    # create and run assistant in a background thread (so FastAPI event loop isn't blocked)
    global assistant
    assistant = PicoAssistant(ws_manager=ws_manager)
    t = threading.Thread(target=assistant.run, daemon=True)
    t.start()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await ws_manager.connect(websocket)


# backend/main.py
import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=5000, reload=True)
