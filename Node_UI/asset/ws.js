var wsUri = "ws://127.0.0.1:7777";
var output;

function Websocket_init()
{
    websocket = new WebSocket(wsUri);
  websocket.onopen = function(evt) { onOpen(evt) };
  websocket.onclose = function(evt) { onClose(evt) };
  websocket.onmessage = function(evt) { onMessage(evt) };
  websocket.onerror = function(evt) { onError(evt) };
}

function onOpen(evt)
{
 
}

function onClose(evt)
{
 
}

function onMessage(evt)
{
    var data = atob(evt.data);
    data = JSON.parse(data)
 console.log("Get_MEssage:"+data)

    switch (data["order"]) {
        case "notify":
                window.app.show_the_girl(data['detail'])
            break;
    
        default:
            break;
    }
}

function onError(evt)
{
 
}

function doSend(message)
{
  
}
