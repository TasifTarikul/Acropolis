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
          $( this ).addClass( "input-border-bottom" );
          $(".input-icon-class", this).addClass("input-icon-hover")
        }, function() {
          $( this ).removeClass( "is-focused" );
          $( this ).removeClass( "input-border-bottom" );
          $(".input-icon-class", this).removeClass("input-icon-hover")
        }
    )

    $(".single-group-box").hover(
       function() {
          $( this ).addClass( "is-focused" );
          $( this ).addClass( "input-border-bottom" );
          $(".input-icon-class1", this).addClass("input-icon-hover1")
        }, function() {
          $( this ).removeClass( "is-focused" );
          $( this ).removeClass( "input-border-bottom" );
          $(".input-icon-class1", this).removeClass("input-icon-hover1")
        }
    )

    // main body form input hover

    $(".main-body-form-list").hover(
       function() {
          $( this ).addClass( "is-focused" );
          $( this ).addClass( "input-border-bottom" );
        }, function() {
          $( this ).removeClass( "is-focused" );
          $( this ).removeClass( "input-border-bottom" );
        }
    )

    $(".main-body-form-list11").hover(
       function() {
          $( this ).addClass( "is-focused" );
          $( this ).addClass( "input-border-bottom" );
        }, function() {
          $( this ).removeClass( "is-focused" );
          $( this ).removeClass( "input-border-bottom" );
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

    $('.admin-page-menu-listname').click(function() {
        $('.admin-page-menu-listname').removeClass('activeadmin');
        $(this).addClass('activeadmin');
    }); 


    //tabel icons
     $(".admin-page-table-icon").click(function(){
        $(this).toggleClass("fa-chevron-circle-down fa-chevron-circle-up");
     }) 



     // login form input hover
    $(".single-group-box1").hover(
       function() {
          $( this ).addClass( "is-focused" );
          $( this ).addClass( "input-border-bottom" );
          $(".input-icon-class", this).addClass("input-icon-hover")
        }, function() {
          $( this ).removeClass( "is-focused" );
          $( this ).removeClass( "input-border-bottom" );
          $(".input-icon-class", this).removeClass("input-icon-hover")
        }
    )

    $(".single-group-box1").hover(
       function() {
          $( this ).addClass( "is-focused" );
          $( this ).addClass( "input-border-bottom" );
          $(".input-icon-class1", this).addClass("input-icon-hover1")
        }, function() {
          $( this ).removeClass( "is-focused" );
          $( this ).removeClass( "input-border-bottom" );
          $(".input-icon-class1", this).removeClass("input-icon-hover1")
        }
    )


    // login form input hover

    $(".main-body-form-list1").hover(
       function() {
          $( this ).addClass( "is-focused" );
          $( this ).addClass( "input-border-bottom" );
          $( "label",this ).addClass( "myfromsize" );
        }, function() {
          $( this ).removeClass( "is-focused" );
          $( this ).removeClass( "input-border-bottom" );
          $( "label",this ).addClass( "myfromsize" );
        }
    )

    //checkbox click

    $('.checkbox-one').on('click', function() {
        $('.checkbox-one').prop('checked', false);  
        $(this).prop('checked', true);
    });

    $('.checkbox-two').on('click', function() {
        $('.checkbox-two').prop('checked', false);  
        $(this).prop('checked', true);
    });

    $('.checkbox-three').on('click', function() {
        $('.checkbox-three').prop('checked', false);  
        $(this).prop('checked', true);
    });

    $('.checkbox-four').on('click', function() {
        $('.checkbox-four').prop('checked', false);  
        $(this).prop('checked', true);
    });


    // real time show input value
    $('.form-input-fullname').keyup(function () {
        $('.form-input-fullname-value').val($(this).val());
    });

    $('.form-input-passport').keyup(function () {
        $('.form-input-passport-value').val($(this).val());
    });

    $('.form-input-place').keyup(function () {
        $('.form-input-place-value').val($(this).val());
    });

    
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