from config import *
import websocket, json

def on_open(ws):
    print("opened")

socket = "wss://data.alpaca.markets/stream"
ws = websocket.WebSocketApp(socket, on_open=on_open)
ws.run_forever()

# yeah I think it only opens then 