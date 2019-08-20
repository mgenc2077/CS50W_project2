document.addEventListener('DOMContentLoaded', () => {
    alert("yüklendi")
    document.querySelector("#form").onsubmit = function() {    
        // Connect to websocket
        var socket = io.connect('http://127.0.0.1:5000/');

        // When connected, configure buttons
        socket.on('connect', () => {
            const msg = document.querySelector("#Kanal_adi").innerHTML;
            //const kanal_no = document.querySelector("#Kanal_No").value;
            socket.emit("baglanti", {"msg":msg});
        });
    };
});
