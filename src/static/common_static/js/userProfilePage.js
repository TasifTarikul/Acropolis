$(document).ready(function(){
	$('.infoField').on('keypress', function(e){
		if (e.which==13){	//to detect if enter is pressed
			console.log('enter pressed')
			$(this).blur()	//to remove focus from input field
		}
	})
})
