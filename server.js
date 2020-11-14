const WebSocket = require("ws");

const port = 55666;
const wss = new WebSocket.Server({ port: port });

console.log(`Server run at port => ${port}`);
wss.on("connection", (ws) => {
  ws.on("message", (message) => {
    console.log(`Received message => ${message}`);
    ws.broadcast(`Server send: ${message}`);
  });
});
