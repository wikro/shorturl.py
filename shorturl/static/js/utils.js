function check_paste() {
	var url_input = document.getElementById('url');
	var form = document.getElementById('form');

	if(url_input.value == '') {
		setTimeout(check_paste, 10);
	} else {
		form.submit();
	}
}
