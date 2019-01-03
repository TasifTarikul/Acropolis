$(document).ready(function(){

		var htmlstring = "";
    var paginationstring = "";
		var nutrition_api_url =  'http://localhost:8000/superAdmin/api/list/';
    var data



    
    //filter function  
 		var get_value = function(data, def_url){

 			data = data || {};
      def_url = def_url || nutrition_api_url;

      if(typeof data['page_size'] == 'undefined')
          {
              data['page_size'] = 25
          }
      

 	    $.ajax({
              url: nutrition_api_url, 
              type: "GET",
              dataType: "json",
              data: data,
              success: function(data){
                console.log(data.results)
                htmlstring = ""

              $.map(data['results'], function(val, i){



              		htmlstring += "<tr class='main-body-table-value'>"
              		+"<td><span>"+val.id+"</span></td>"
              		+"<td><span>"+val.full_name+"</span></td>"
              		+"<td><span>"+val.email+"</span></td>"
              		+"<td><span>"+val.phone_no+"</span></td>"
              		+"<td><span>"+val.country_of_residence+"</span></td>"
              		+"<td><span>"+val.nationality+"</span></td>"
              		+"<td><span>"+val.his_age+"</span></td>"
              		+"<td><span>"+val.gender+"</span></td>"
              		+"<td><span>"+val.passport_no+"</span></td>"
              		+"<td><span>"+val.date_joined+"</span></td>"

              		+"<td>"
              		+"<select class='form-tabel-status'>"
              		+"<option>"+val.client_status+"</option>"
              		+"</select>"
              		+"<i class='fas fa-sort-down input-icon-class2'></i>"
              		+"</td>"

              		+"<td><span>"+val.application_status+"</span></td>"
              		+"<td><span>"+val.application_type+"</span></td>"

              		+"</tr>"


              })  


                // $(".addTheValues").html('')
                $(".addTheValues").html(
                    htmlstring
                  )
                // $(".addTheValues").html(
                //     htmlstring
                //   )

              paginationstring = ""
              $.map(data['pagination']['page_range'], function(val, i){ 
                  paginationstring += "<li class='paginationClass' data-page='"+val +"'><span>"+val+"</span></li>"
              })


                $(".main-body-pagination-list").html(
                    paginationstring
                  ) 

              }     

          })

     	 }

     	 get_value() 


     	 //click the ASE & DESE
     	 $(".admin-page-table-icon").click(function(){
     	 	 var attrvalue = $(this).attr('data-order-by-status')
     	 	 var attrname = $(this).attr('data-name')
             if(attrvalue == "asc"){
             	$(this).attr('data-order-by-status','desc')
             	console.log(attrvalue)
             	console.log(attrname)
             }else{
             	$(this).attr('data-order-by-status','asc')
             	console.log(attrvalue)
             	console.log(attrname)
             }
             
             data = {}
             data[attrname] = attrvalue
       
	        get_value(data)


     	 })	



     	 //search box enter
     	 $('.searchBoxDate').keypress(function (e) {
			 var key = e.which;
			 var searchInputValue;
			 if(key == 13)  // the enter key code
			  {
			  	var attrname = $(this).attr('data-name')
			  	searchInputValue = $(this).val()
			    console.log(searchInputValue)
			    console.log(attrname)

			    data = {}
             	data[attrname] = searchInputValue
       
	        	get_value(data)

			  }
		});


     	//search box enter age
     	 $('.ageValue').keypress(function (e) {
			 var key = e.which;
			 if(key == 13)  // the enter key code
			  {
			  	var attrname1 = $(".formAge").attr('data-name')
			  	var attrname2 = $(".toAge").attr('data-name')
			  	var searchInputValue1 = $(".formAge").val()
			  	var searchInputValue2 = $(".toAge").val()
    			
    			data = {}

			    if(searchInputValue1 == "" && searchInputValue2 != ""){
			    	data[attrname2] = searchInputValue2
			    }else if(searchInputValue1 != "" && searchInputValue2 == ""){
			    	data[attrname1] = searchInputValue1
			    }else if(searchInputValue1 != "" && searchInputValue2 != ""){
			    	data[attrname1] = searchInputValue1
			    	data[attrname2] = searchInputValue2
			    }else{

			    }
			    
			    get_value(data)

			  }
		}); 


     	//search box enter date
     	$(".dateValue").change(function(){
     		var attrname1 = $("#datepicker1").attr('data-name')
			var attrname2 = $("#datepicker2").attr('data-name')
     		var datevalue1 = $("#datepicker1").val()
     		var datevalue2 = $("#datepicker2").val()
     		console.log(datevalue1)
     		console.log(datevalue2)
     		console.log(attrname1)
     		console.log(attrname2)

     		data = {}

     		if(datevalue1 == "" && datevalue2 != ""){
			    	data[attrname2] = datevalue2
			}else if(datevalue1 != "" && datevalue2 == ""){
			    	data[attrname1] = datevalue1
			}else if(datevalue1 != "" && datevalue2 != ""){
			    	data[attrname1] = datevalue1
			    	data[attrname2] = datevalue2
			}else{

			    }
			    
			    get_value(data)

     	})

      


     	 //onclick the option 
     	 $(".main-table-optionbox").click(function(){
     	 	var attrname = $(this).attr('data-name')
     	 	var selectedValue = $("option:selected",this ).text();
     	 	 console.log(attrname)
     	 	 console.log(selectedValue)
     	 	 data = {}
             data[attrname] = selectedValue
       
	         get_value(data)
     	 })

     	 //onclick the option 
     	 $(".submain-table-optionbox").click(function(){
     	 	var attrname = $(this).attr('data-name')
     	 	var selectedValue = $("option:selected",this ).text();
     	 	 console.log(attrname)
     	 	 console.log(selectedValue)
     	 	 data = {}
             data[attrname] = selectedValue
       
	         get_value(data)
     	 })

     	 //onclick the option 
     	 $(".submain2-table-optionbox").click(function(){
     	 	var attrname = $(this).attr('data-name')
     	 	var selectedValue = $("option:selected",this ).text();
     	 	 console.log(attrname)
     	 	 console.log(selectedValue)
     	 	 data = {}
             data[attrname] = selectedValue
       
	         get_value(data)
     	 })



       //pagination request send
        $(document).on('click', '.paginationClass', function() {
           var paginationValue = $(this).attr("data-page")
           console.log(paginationValue)

           if(typeof data == 'undefined'){
             data = {}
           }
           data['page'] = paginationValue
           get_value(data)
       })


       

       $('.page-range-select').change(function() {
          var $option = $(this).find('option:selected');
          var value = $option.val();//to get content of "value" attrib

          if(typeof data == 'undefined'){
              var data = {}
          }
          data['page_size'] = value
          console.log('data ', data)
          get_value(data)
          
          console.log(value)
      });



   	})
