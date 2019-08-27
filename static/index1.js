document.addEventListener('DOMContentLoaded', () => {
    // Çıkış butonu:
    document.querySelector('#cikis').onclick = () => {
        localStorage.removeItem('nick');
        alert('Çıkış Tamamlandı');
    }
    // Giriş butonu:
    document.querySelector('#giris').onclick = () => {
        let nick = document.querySelector('#Kanal_Adi').value;
        localStorage.setItem('nick', nick);
        alert('Giriş Tamamlandı');
    }
    // kanal listesi yenileme butonu:
    document.querySelector('#refresh').onclick = () => {
        const request = new XMLHttpRequest();
        const kanal = document.querySelector('#channel').value;
        console.log({ kanal })
        request.open('POST', '/channel_list');
        request.onload = () => {
            const kanal_listesi = JSON.parse(request.responseText)
            const kan_lis = kanal_listesi['channel']
            var i;
            console.log({ kanal_listesi })
            for (i = 0; i < kan_lis.length; i++) {
                document.querySelector('ol#ajaxx').innerHTML += i + " &nRightarrow; " + kan_lis[i] + "<br>";
            };
        }
        const data = new FormData();
        data.append('currency', kanal);
        request.send(data);
    }
    // Chat geçmişi:
    document.querySelector('#yenile').onclick = geri;
    // nick ve kanal  numarasının localstorage üzerinden hatırlanması:
    if (localStorage.getItem('nick') != undefined) {
        document.querySelector('#Kanal_Adi').value = localStorage.getItem('nick');
    }
    if (localStorage.getItem('channel') != undefined) {
        document.querySelector('#channel').value = localStorage.getItem('channel');
    }
    // Websocket link bağlantısı:
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    socket.on('connect', () => {
        // bağlandı mesajı:
        socket.emit('baglanti', {
            data: 'Kullanici Baglandi'
        });
        //formdan veri alınması:
        document.querySelector('form').onsubmit = ( e ) => {
            e.preventDefault();
            let kanal_adi = document.querySelector('#Kanal_Adi').value;
            let kanal_no = document.querySelector('#Kanal_No').value;
            let channel = document.querySelector('#channel').value;
            console.log({ kanal_adi, kanal_no, channel })
            // server'a veri gönderilmesi:
            socket.emit('test', {
                kullanici_adi : kanal_adi,
                kanal_no : kanal_no,
                channel : channel
            });
            document.querySelector('#Kanal_No').value = ''
        };
    });
    // Gelen verilerin gösterilmesi:
    socket.on('gonder', ( msg ) => {
        console.log( msg )
        if( typeof msg.kullanici_adi !== 'undefined' ) {
            document.querySelector('ul#messages').innerHTML += "<li>" + msg.zaman + " &rAarr; " +  msg.kullanici_adi  + " &nRightarrow; " + msg.kanal_no +"</li>";
        }
    })
})
// geçmiş'in yüklenmesi:
function geri() {
    const request = new XMLHttpRequest();
    const rinne = document.querySelector('#channel').value;
    console.log({ rinne });
    request.open('POST', '/mesajlist');
    request.onload = () => {
        const random = JSON.parse(request.responseText);
        const mes_lis = random['gecmis'];
        var i;
        console.log({ mes_lis });
        for (i = 0; i < mes_lis.length; i++) {
            let temp = Object.values(mes_lis[i])
            console.log({ temp })
            document.querySelector('ul#messages').innerHTML += "<li>" + temp[2] + " &rAarr; " +  temp[0]  + " &nRightarrow; " + temp[1] +"</li>";
        };
    }
    const data = new FormData();
    data.append('history', rinne);
    request.send(data);
}