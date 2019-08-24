document.addEventListener('DOMContentLoaded', () => {
    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    socket.on('connect', () => {
        socket.emit('baglanti', {
            data: 'User Connected'
        } )
        var form1 = $( 'form' ).on( 'submit', function( e ) {
            e.preventDefault()
            let user_name = $( 'input.username' ).val()
            let user_input = $( 'input.message' ).val()
            socket.emit( 'test', {
              user_name : user_name,
              message : user_input
            } )
            $( 'input.message' ).val( '' ).focus()
        } )
    });
    socket.on('gonder', ( msg ) => {
        console.log( msg )
        if( typeof msg.user_name !== 'undefined' ) {
            $( 'h3' ).remove()
            $( 'div.message_holder' ).append( '<div><b style="color: #000">'+msg.user_name+'</b> '+msg.message+'</div>' )
        }
    });
});
