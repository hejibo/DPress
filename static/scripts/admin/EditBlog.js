window.onload = function() { 
	var markup = document.getElementById('id_markup');
	addEvent(markup, 'change', function() {
		if (markup.value=='html') InitTinyMCE();
	});
	if (markup.value=='html') InitTinyMCE();
}
