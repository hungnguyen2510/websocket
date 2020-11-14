import asyncio
import websockets


# host= "localhost"
host = "118.69.126.48"
port = "55666"


async def ClientSend():
    uri = "ws://"+host+":"+port
    async with websockets.connect(uri) as websocket:
        s = input("Input: ")

        await websocket.send(s)
        print(f"> {s}")

        res = await websocket.recv()
        print(f"< {res}")

asyncio.get_event_loop().run_until_complete(ClientSend())
