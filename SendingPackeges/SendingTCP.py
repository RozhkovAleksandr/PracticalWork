import asyncio
import websockets

bytes = 400
num_of_packages = 7200
interval = 0.05

async def send_packets():
    uri = "ws://192.168.1.102"
    payload = b'x' * bytes

    async with websockets.connect(uri) as websocket:
        for _ in range(num_of_packages):
            await websocket.send(payload)
            await asyncio.sleep(interval)

asyncio.run(send_packets())