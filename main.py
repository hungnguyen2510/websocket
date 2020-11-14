import asyncio
from webSocketClient import WebSocketClient

if __name__ == '__main__':
    # Creating client object
    client = WebSocketClient()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(client.connect(host='118.69.126.48',port='55666'))
    loop.run_forever()
    loop.close()