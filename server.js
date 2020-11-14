const WebSocket = require("ws");

const port = 8080;
const wss = new WebSocket.Server({ port: port });

console.log(`Server run at port => ${port}`);
wss.on("connection", (ws) => {
  ws.on("message", (message) => {
    console.log(`Received message => ${message}`);
    ws.send(`Server send: ${message}`);
  });
});
