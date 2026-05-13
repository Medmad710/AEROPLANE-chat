import asyncio
import websockets
import json
import os

HISTORY_FILE = "messages.json"
connected_clients = set()

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_message(msg):
    history = load_history()
    history.append(msg)
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

async def handler(websocket):
    connected_clients.add(websocket)
    try:
        history = load_history()
        await websocket.send(json.dumps({"type": "history", "messages": history}))

        async for raw in websocket:
            data = json.loads(raw)
            msg = {"type": "message", "sender": data["sender"], "text": data["text"]}
            save_message(msg)
            websockets.broadcast(connected_clients, json.dumps(msg))
    except websockets.ConnectionClosed:
        pass
    finally:
        connected_clients.discard(websocket)

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("Server started on ws://localhost:8765")
        await asyncio.Future()

asyncio.run(main())
