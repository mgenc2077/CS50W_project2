document.addEventListener('DOMContentLoaded', () => {
    // Çıkış butonu
    document.querySelector('#cikis').onclick = () => {
        localStorage.removeItem('nick');
        alert('Çıkış Tamamlandı');
    }
    // Giriş butonu
    document.querySelector('#giris').onclick = () => {
        let nick = document.querySelector('#Kanal_Adi').value;
        localStorage.setItem('nick', nick);
        alert('Giriş Tamamlandı');
    }
    // Websocket link bağlantısı
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    socket.on('connect', () => {
        // bağlandı mesajı
        socket.emit('baglanti', {
            data: 'Kullanici Baglandi'
        });
        // Giriş ekranında adı hatırlama
        if (localStorage.getItem('nick')) {
            document.querySelector('#Kanal_Adi') = localStorage.getItem('nick');
        }
        //formdan veri alınması
        document.querySelector('form').onsubmit = ( e ) => {
            e.preventDefault();
            let kanal_adi = document.querySelector('#Kanal_Adi').value;
            let kanal_no = document.querySelector('#Kanal_No').value;
            let channel = document.querySelector('#channel').value;
            console.log({ kanal_adi, kanal_no, channel})
            // server'a veri gönderilmesi
            socket.emit('test', {
                kullanici_adi : kanal_adi,
                kanal_no : kanal_no,
                channel : channel
            });
        };
    });
    socket.on('gonder', ( msg ) => {
        console.log( msg )
        if( typeof msg.kullanici_adi !== 'undefined' ) {
            document.querySelector('ol#messages').innerHTML += "<li>" +  msg.kullanici_adi  + " &nRightarrow; "+ msg.kanal_no +"</li>";
        }
    })
})