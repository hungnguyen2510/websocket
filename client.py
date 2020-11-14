import asyncio
import websockets


port = 8080
async def test():
    uri = "ws://localhost:"+str(port)
    async with websockets.connect(uri) as websocket:
        s = input("Input: ")

        await websocket.send(s)
        print(f"> {s}")

        res = await websocket.recv()
        print(f"< {res}")

asyncio.get_event_loop().run_until_complete(test())