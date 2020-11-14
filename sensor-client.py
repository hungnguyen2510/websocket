import asyncio
import websockets


port = 55666
async def test():
    uri = "ws://118.69.126.48:"+str(port)
    async with websockets.connect(uri) as websocket:
        s = input("Input: ")

        await websocket.send(s)
        print(f"> {s}")

        res = await websocket.recv()
        print(f"< {res}")

asyncio.get_event_loop().run_until_complete(test())