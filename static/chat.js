jQuery(document).ready( function ( $ ) {
	var $body = $("#body"),
	    $send = $("#send"),
	    $mesg = $("#messages");

	var conversation = document.cookie;
	if( conversation.length == 0 ) {
		conversation = navigator.appVersion + Math.random() + new Date();
		conversation = conversation.replace( /\W+/g, '' );
		document.cookie = "conversation=" + escape( conversation ) + "; path=/";
	}
	else {
		conversation = conversation.split( '=' );
		conversation = conversation[1];
	}

	$send.click( function () {
		var val = $body.val().replace( /^\s+|\s+$/g, '' );
		if( val.length <= 0 ) { return; }
		$body.val('');
		$mesg.append( $('<div/>').addClass('me').text(val) );
		$.get(
			'/chat.txt',
			{ conversation: conversation, body: val }
		).success( function ( data ) {
			$mesg.append( $('<div/>').addClass('don').text(data) );
		} ).error( function ( xhr ) {
			$mesg.append( $('<div/>').addClass('don').text('ERROR!') );
		} );
		$body.focus();
	} );

	$body.keypress( function ( e ) {
		if( e.which == 13 ) { $send.click(); return false; }
	} );
} );
