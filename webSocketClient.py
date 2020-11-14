import websockets

class WebSocketClient():

    def __init__(self):
        pass

    async def connect(self,host,port):
        '''
            Connecting to webSocket server

            websockets.client.connect returns a WebSocketClientProtocol, which is used to send and receive messages
        '''
        self.connection = await websockets.client.connect('ws://'+host+':'+port+'')
        print(host,port)
        if self.connection.open:
            print('Connection stablished. Client correcly connected')
            # Send greeting
            await self.sendMessage('Hey server, this is webSocket client')
            # Enable listener
            await self.receiveMessage()


    async def sendMessage(self, message):
        '''
            Sending message to webSocket server
        '''
        await self.connection.send(message)

    async def receiveMessage(self):
        '''
            Receiving all server messages and handling them
        '''
        while True:
            message = await self.connection.recv()
            print('Received message from server: ' + str(message))