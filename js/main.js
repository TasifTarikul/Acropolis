$(document).ready(function(){

   //mobile menu toggle button
    $("#mobile-menu-button").click(function(){
     
       $("#mobile-menu-list").show(500);
       $("#mobile-menu-button").css('display','none')
       $("#mobile-menu-button1").css('display','block')

    });
    
    //pciture edit button hover
    $(".pic-update-edit").hover(
        function() {
          $( this ).css( "color", "#3f51b5" );
        }, function() {
          $( this ).css( "color", "#bebebe" );
        }
      )

    $("#mobile-menu-button1").click(function(){
     
       $("#mobile-menu-list").hide(500);
       $("#mobile-menu-button").css('display','block')
       $("#mobile-menu-button1").css('display','none')

    });


    //profile form toggle
    $(".body-profile-details").click(function(){
        $(".body-profile-input-box").slideToggle("slow")
        $(".about-arrow-down").toggleClass("fa-angle-down fa-angle-up");
    })

    // add company toggle
    $(".body-profile-details-2").click(function(){
        $(".side-add-company").slideToggle("slow")
        $(".about-arrow-down-2").toggleClass("fa-angle-down fa-angle-up");

    })

    // profile form input hover
    $(".single-group-box").hover(
       function() {
          $( this ).addClass( "is-focused" );
          $(".input-icon-class", this).addClass("input-icon-hover")
        }, function() {
          $( this ).removeClass( "is-focused" );
          $(".input-icon-class", this).removeClass("input-icon-hover")
        }
    )

    // main body form input hover

    $(".main-body-form-list").hover(
       function() {
          $( this ).addClass( "is-focused" );
        }, function() {
          $( this ).removeClass( "is-focused" );
        }
    )
    
    // form collpase icon toggle
    $(".form-button-text1").click(function(){
        $(".about-arrow-down1").toggleClass("fa-angle-down fa-angle-up");
        $(".about-arrow-down2").addClass("fa-angle-down ");
        $(".about-arrow-down3").addClass("fa-angle-down ");
        $(".about-arrow-down2").removeClass("fa-angle-up ");
        $(".about-arrow-down3").removeClass("fa-angle-up ");
    })

    $(".form-button-text2").click(function(){
        $(".about-arrow-down2").toggleClass("fa-angle-down fa-angle-up");
        $(".about-arrow-down1").addClass(" fa-angle-down ");
        $(".about-arrow-down3").addClass("fa-angle-down ");
        $(".about-arrow-down1").removeClass("fa-angle-up ");
        $(".about-arrow-down3").removeClass("fa-angle-up ");
    })

    $(".form-button-text3").click(function(){
        $(".about-arrow-down3").toggleClass("fa-angle-down fa-angle-up");
        $(".about-arrow-down1").addClass("fa-angle-down ");
        $(".about-arrow-down2").addClass("fa-angle-down ");
        $(".about-arrow-down1").removeClass("fa-angle-up ");
        $(".about-arrow-down2").removeClass("fa-angle-up ");
    })

    $('.main-body-menu-listname').click(function() {
        $('.main-body-menu-listname').removeClass('main-body-menu-active');
        $(this).addClass('main-body-menu-active');
    });

    $('[data-toggle="tooltip"]').tooltip();   
    
    /*
    $(".input-box-class").keyup(function(){
        
      if($(".single-group-box").hasClass("is-filled") == true){
            $(".input-icon-class").addClass("input-icon-hover")
      }else{
            $(".input-icon-class").removeClass("input-icon-hover")
      }

    })
   
    //open the submenu
    $("#singup-list li").mouseover(function(){
		    $(".logout-box").css('display','block')
    })

    $("#singup-list li").mouseleave(function(){

    	$(".logout-box").css('display','none')

    })

    //open the submenu
    $(".logout-box").mouseover(function(){
        $(this).css('display','block')
    })

    $(".logout-box").mouseleave(function(){

      $(this).css('display','none')

    })*/


})


$(document).scroll(function() {
	//Main Menu
           if($(window).scrollTop() > 50){

            $("#main-menu").css("background","#052738");
 
           }else if($(window).scrollTop() < 50){

            $("#main-menu").css("background","");
  
           }

    //Mobile menu
           if($(window).scrollTop() > 50){

            $("#mobile-menu").css("background","#052738");
 
           }else if($(window).scrollTop() < 50){

            $("#mobile-menu").css("background","");
  
           }
       
    });