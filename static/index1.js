document.addEventListener('DOMContentLoaded', () => {
    // Websocket link bağlantısı
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    socket.on('connect', () => {
        socket.emit('baglanti', {
            data: 'Kullanici Baglandi'
        });
        document.querySelector('form').onsubmit = ( e ) => {
            e.preventDefault();
            let kanal_adi = document.querySelector('#Kanal_Adi').value;
            let kanal_no = document.querySelector('#Kanal_No').value;
            socket.emit('test', {
                kullanici_adi : kanal_adi,
                kanal_no : kanal_no
            });
        };
    });
    socket.on('gonder', ( msg ) => {
        console.log( msg )
        if( typeof msg.kullanici_adi !== 'undefined' ) {
            // document.querySelector('h3').innerHTML = msg.kullanici_adi + msg.kanal_no
            document.querySelector('ol#messages').innerHTML += "<li>" +  msg.kullanici_adi  + " &nRightarrow; "+ msg.kanal_no +"</li>";
        }
    })
})