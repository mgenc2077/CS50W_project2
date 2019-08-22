document.addEventListener('DOMContentLoaded', () => {
    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    socket.on('connect', () => {
        document.querySelector("#tus").onclick =() => {    
            if (!localStorage.getItem('anan')) {
                var anan = document.querySelector('#Kanal_Adi').value;
                localStorage.setItem('anan', anan);
            }
            if (localStorage.getItem('anan') != document.querySelector('#Kanal_Adi').value) {
                var anan = document.querySelector('#Kanal_Adi').value;
                localStorage.setItem('anan', anan);
            }
            var eben = localStorage.getItem('anan');
            console.log({ eben });
            socket.emit('baglanti', {'eben': eben});
        };
    });
    socket.on('gonder', data => {
        const li = document.createElement('li');
        li.innerHTML = `kanal adi: ${data.eben}`;
        document.querySelector('#yazi').append(li);
    });
});
