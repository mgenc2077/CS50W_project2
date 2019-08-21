document.addEventListener('DOMContentLoaded', () => {
    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    socket.on('connect', () => {
        document.querySelector("#form").onsubmit = function() {    
            if (!localStorage.getItem('anan')){
                var anan = document.querySelector('#Kanal_Adi').value;
                localStorage.setItem('anan', anan);
            }
            eben = localStorage.getItem('anan')
            alert(`hello ${eben}!`)
            socket.emit('baglanti', {'eben': eben});
        };
    });
    socket.on('gonder', data => {
        const li = document.createElement('li');
        li.innerHTML = `kanal adi: ${data.eben}`;
        document.querySelector('#yazi').append(li);
    });
});
