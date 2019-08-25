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
    const request = new XMLHttpRequest();
    const kanal = document.querySelector('#channel').value;
    console.log({ kanal })
    request.open('POST', '/channel_list');
    
    request.onload = () => {
        const kanal_listesi = JSON.parse(request.responseText)
        var i;
        for (i = 0; i < kanal_listesi.length; i++) {
            document.querySelector('ol#ajaxx').innerHTML += kanal_listesi[i] + "<br>";
        };
    }
    const data = new FormData();
    data.append('currency', kanal);
    request.send(data);

    // Websocket link bağlantısı
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    socket.on('connect', () => {
        // bağlandı mesajı
        socket.emit('baglanti', {
            data: 'Kullanici Baglandi'
        });
        // Giriş ekranında adı hatırlama
        if (localStorage.getItem('nick')) {
            document.querySelector('#Kanal_Adi').innerHTML = localStorage.getItem('nick');
        }
        if (localStorage.getItem('channel')) {
            document.querySelector('#channel').innerHTML = localStorage.getItem('channel');
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