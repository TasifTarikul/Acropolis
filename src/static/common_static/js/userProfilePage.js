$(document).ready(function(){





/*****************************************
			Birth Certificate
*****************************************/
	
	// add new files

	$('.addBirthCertificateFileOnList').on('change', function(e){
		$('.ListOfNewBirthCertificateFile').html('')
		files = e.target.files
		var files = Array.prototype.slice.call(files);
		files.forEach(function(file) {
		test_htmls = '<span class="current_birth_certificate_file">'+file.name+'</span><span class="update_newly_added_birth_certificate_file"> <i class="fas fa-times close-file-icon"></i></span></span></br>'
		$('.ListOfNewBirthCertificateFile').append(test_htmls)
		});

		$('.update_newly_added_birth_certificate_file').on('click', function(){
			$('.addBirthCertificateFileOnList').trigger('click')
		})
	})


	// update already existing files
	var crnt_birth_certificate_value = $('.currentBirthCertificateFiles').val()	
	var birth_certificate = JSON.parse(crnt_birth_certificate_value);

	$('.current_birth_certificate_file').on('click', function(){
		clicked_id = $(this).data('id')
		index = birth_certificate.indexOf(clicked_id)

		if(index!=-1){
		   birth_certificate.splice(index, 1);
		}
		$(this).parent().remove()
	})
	

	
	$('.UploadBirthCertificateFile').on('click', function(e){		//final submit
		$('.currentBirthCertificateFiles').val(birth_certificate)	//add latest value of file id after removing from list to the input field
	})



/*****************************************
				End
*****************************************/









/*****************************************
			Marriage Certificate
*****************************************/
	
	// add new files

	$('.addMarriageCertificateFileOnList').on('change', function(e){
		$('.ListOfNewMarriageCertificateFile').html('')
		files = e.target.files
		var files = Array.prototype.slice.call(files);
		files.forEach(function(file) {
		test_htmls = '<span class="current_marriage_certificate_file">'+file.name+'</span><span class="update_newly_added_marriage_certificate_file"> <i class="fas fa-times close-file-icon"></i></span></br>'
		$('.ListOfNewMarriageCertificateFile').append(test_htmls)
		});

		$('.update_newly_added_marriage_certificate_file').on('click', function(){
			$('.addMarriageCertificateFileOnList').trigger('click')
		})
	})


	// update already existing files
	var crnt_marriage_certificate_value = $('.currentMarriageCertificateFiles').val()	
	var current_marriage_certificate_file_ids = JSON.parse(crnt_marriage_certificate_value);

	$('.current_marriage_certificate_file').on('click', function(){
		clicked_id = $(this).data('id')
		index = current_marriage_certificate_file_ids.indexOf(clicked_id)

		if(index!=-1){
		   current_marriage_certificate_file_ids.splice(index, 1);
		}
		$(this).parent().remove()
	})
	

	
	$('.uploadMarriageCertificateFile').on('click', function(e){		//final submit
		$('.currentMarriageCertificateFiles').val(current_marriage_certificate_file_ids)	//add latest value of file id after removing from list to the input field
	})



/*****************************************
				End
*****************************************/












/*****************************************
			Passport Copy
*****************************************/
	
	// add new files
	$('.addPassportCopyFileOnList').on('change', function(e){
		$('.ListOfNewPassportCopyFile').html('')
		files = e.target.files
		var files = Array.prototype.slice.call(files);
		files.forEach(function(file) {
		test_htmls = '<span class="current_passport_copy_file">'+file.name+'</span><span class="update_newly_added_passport_copy_file"><i class="fas fa-times close-file-icon"></i></span></br>'
		$('.ListOfNewPassportCopyFile').append(test_htmls)
		});

		$('.update_newly_added_passport_copy_file').on('click', function(){
			$('.addPassportCopyFileOnList').trigger('click')
		})
	})


	// update already existing files
	var crnt_passport_copy_value = $('.currentPassportCopyFiles').val()	
	var current_passport_copy_file_ids = JSON.parse(crnt_passport_copy_value);

	$('.current_passport_copy_file').on('click', function(){
		clicked_id = $(this).data('id')
		index = current_passport_copy_file_ids.indexOf(clicked_id)

		if(index!=-1){
		   current_passport_copy_file_ids.splice(index, 1);
		}
		$(this).parent().remove()
	})
	

	
	$('.uploadPassportCopyFile').on('click', function(e){		//final submit
		$('.currentPassportCopyFiles').val(current_passport_copy_file_ids)	//add latest value of file id after removing from list to the input field
	})



/*****************************************
				End
*****************************************/









/*****************************************
			Bank Statement
*****************************************/
	
	// add new files

	$('.addBankStatementFileOnList').on('change', function(e){
		$('.ListOfNewBankStatementFile').html('')
		files = e.target.files
		var files = Array.prototype.slice.call(files);
		files.forEach(function(file) {
		test_htmls = '<span class="current_bank_statement_file">'+file.name+'</span><span class="update_newly_added_bank_statement_file"><i class="fas fa-times close-file-icon"></i></span></br>'
		$('.ListOfNewBankStatementFile').append(test_htmls)
		});

		$('.update_newly_added_bank_statement_file').on('click', function(){
			$('.addBankStatementFileOnList').trigger('click')
		})
	})


	// update already existing files
	var crnt_bank_statement_value = $('.currentBankStatementFiles').val()	
	var current_bank_statement_file_ids = JSON.parse(crnt_bank_statement_value);

	$('.current_bank_statement_file').on('click', function(){
		clicked_id = $(this).data('id')
		index = current_bank_statement_file_ids.indexOf(clicked_id)

		if(index!=-1){
		   current_bank_statement_file_ids.splice(index, 1);
		}
		$(this).parent().remove()
	})
	

	
	$('.uploadBankStatementFile').on('click', function(e){		//final submit
		$('.currentBankStatementFiles').val(current_bank_statement_file_ids)	//add latest value of file id after removing from list to the input field
	})



/*****************************************
				End
*****************************************/









	
	/*****************************************
	Upload Profile Pic with perfect ratio 3.5cm:5cm
	******************************************/

	$('.profilePicUploadButton').on('click', function(){	//onclick pencil font open/pop up for file input field
		$('.profilePicFileInput').trigger('click')
	})

	function readURL(input) {	//function that handle selected image preview and check it's width:height ration

	  if (input.files && input.files[0]) {

	  		selected_image_ratio = 0

		    var reader = new FileReader();

		    reader.onload = function(e) {
		     var img = new Image();
			 img.onload = function(){		//to get the file info(width/height), for preview no need this part just call the class and add attr>src e.target.result like we did below
			  	var selected_image_ratio = img.width/img.height

			  	$('.mainProfilePic').attr('src', e.target.result);
			  	if (selected_image_ratio<.8 && selected_image_ratio>.6){	//if ration is correct, correct ration means whatever in beween .7:1. since we have 3.5:5 cm required
			  		$(".profilePicUploadSubmit").attr('style', 'display:block')	//display save button
			  		$(".profilePicUploadMsg").html('')

			  	}else{		//if ratio is incorrect
			  		$(".profilePicUploadSubmit").attr('style', 'display:none')
			  		$(".profilePicUploadMsg").html('Image Should be 3.5cm X 5cm')
			  	}
			  }
			  img.src = e.target.result

		    }
		    reader.readAsDataURL(input.files[0]);

	  }
	}

	$(".profilePicFileInput").change(function() {	//while choosing file(image) call that preview image function
	  readURL(this);	//preview selected image
	});


	$(".profilePicUploadSubmit").on('click', function(){
		$(".profilePicFileSubmit").trigger('click')		//upload now
	})

	/*****************************************
					End
	******************************************/



	/*****************************************
					Remove profile pic option
	******************************************/

	$('.profilePicUploadRemove').on('click', function(){
		$(".profilePicUploadSubmit").attr('style', 'display:block')	//display save button
		$('.mainProfilePic').attr('src', '');		//remove from img src
	})

	/*****************************************
					End
	******************************************/

 
  /*var imgcheck = function(){
  	 $('.infoImg').each(function () {
		    if (this.src.length > 0) {
		        $('.infoImg').css('display','none')
		    }
		});
  }

   imgcheck()*/

	/*****************************************
		Left side user profile update
	******************************************/


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
					// console.log(res)
					that.parent().find('.infoImg').css('opacity','1')
					that.parent().find('.infoImg').attr('src', 'https://www.healthandsafetysigns.co.uk/wp-content/uploads/2017/08/tick.png')
					to_append = 'Done'
					that.parent().find('.infomsgtxt').append(to_append)
					that.parent().find('.infomsgtxt').attr('style', 'color:#4CB444')

				},
				error: function(err){
					// console.log('error holo ' , that)
					// console.log(err.responseText)
					that.parent().find('.infoImg').attr('src', 'https://openclipart.org/download/188486/redcross.svg')
					to_append = err.responseJSON[fieldName][0]
					
					that.parent().find('.infomsgtxt').append(to_append)
					that.parent().find('.infomsgtxt').attr('style', 'color:#FC4747')
				}
			})
			$(this).blur()	//to remove focus from input field
		}


  


	})

	/*****************************************
					End
	******************************************/
  /* if ($("#home-md").hasClass("show")) {
	   $("#home-md").css('display','block')
	}else{
		$("#home-md").css('display','none')
	}*/

   $(".file-upload").click(function(){
   	  $("#home-md").css('display','none')
   	  $("#profile-md").css('display','block')
   })

   $(".form-list-all").click(function(){
   	  $("#home-md").css('display','block')
   	  $("#profile-md").css('display','none')
   })



})
