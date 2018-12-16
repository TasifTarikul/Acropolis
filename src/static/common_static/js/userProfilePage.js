$(document).ready(function(){
	
	$('.infoField').on('keypress', function(e){
		if (e.which==13){	//to detect if enter is pressed
			var that = $(this)	//will change inside success/error of ajax
			var update_url = $('.update_url').val()
			var csrf_token = $('.csrf_token').val()
			var got_value = $(this).val()
			var fieldName = $(this).data('fieldName')
			$(this).parent().find('.infoMsgTxt').html('')

			data = {}
			data[fieldName] = got_value

			$.ajax({
				url: update_url,
				headers: { "X-CSRFToken": csrf_token },
				method: 'PATCH',
				data: data,
				success: function(res){
					console.log(res)
					that.parent().find('.infoImg').attr('src', 'https://www.healthandsafetysigns.co.uk/wp-content/uploads/2017/08/tick.png')
					to_append = 'Done'
					that.parent().find('.infomsgtxt').append(to_append)
					that.parent().find('.infomsgtxt').attr('style', 'color:#4CB444')

				},
				error: function(err){
					console.log('error holo ' , that)
					console.log(err.responseText)
					that.parent().find('.infoImg').attr('src', 'https://openclipart.org/download/188486/redcross.svg')
					to_append = err.responseJSON[fieldName][0]
					
					that.parent().find('.infomsgtxt').append(to_append)
					that.parent().find('.infomsgtxt').attr('style', 'color:#FC4747')
				}
			})
			$(this).blur()	//to remove focus from input field
		}
	})
})
