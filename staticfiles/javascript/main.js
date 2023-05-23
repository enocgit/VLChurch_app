$(function(){

    $('.slider-parent').slick({
        slidesToShow: 3,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 2000,
        centerMode: true,
        arrows: false,
        pauseOnHover: true,
        adaptiveHeight: true,
        responsive: [
            {
              breakpoint: 947,
              settings: {
                slidesToShow: 2,
                slidesToScroll: 2,
              }
            },
            {
              breakpoint: 673,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
              }
            },
            {
              breakpoint: 424,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
              }
            },
          ]
    });
      
    const viewRecap = document.getElementById('view-recap')
    const recapId = viewRecap.dataset.recapId

    document.documentElement.style.setProperty('--animate-duration', '1.5s');    
 
    $('.message-bubble').on('mouseenter', function() {
        // $('.edit-btn').hide()
        $(this).find('.edit-btn').removeClass('invisible')
        $(this).find('.delete-btn').removeClass('invisible')
    })
    $('.message-bubble').on('mouseleave', function() {
        // $('.edit-btn').hide()
        $(this).find('.edit-btn').addClass('invisible')
        $(this).find('.delete-btn').addClass('invisible')
    })
    
    $(window).on({
        scroll: function(){
            let scrollTop = $(window).scrollTop()
            // if (scrollTop >= 178) {
            //     $('#brand-sub').removeClass('invisible')
            // }
            // else {
            //     $('#brand-sub').addClass('invisible')
            // }
            // console.log(scrollTop)
            // if (scrollTop >= 121){
            //     $('#main-nav').addClass('fixed')
            //     $('#main-nav').addClass('w-full')
            //     // $('#main-nav').addClass('mt-40')
            // }
            // else {
            //     $('#main-nav').removeClass('fixed')
            //     $('#main-nav').addClass('mt-3')
            // }
        }
    })

    // $('#online-giving-drawer').on('click', () => {
    //     console.log(2)
    // })

    $('.menu-btn').on({
        mouseover: function(){
            $('.menu-btn-text').css({'visibility':'visible'})
            // $('.menu-btn-text').addClass('animate__animated animate__zoomInUp')
        },
        mouseleave: function(){
            $('.menu-btn-text').css({'visibility':'hidden'})
            // $('.menu-btn-text').addClass('animate__animated animate__lightSpeedOutRight')
        }
    })
    
    // var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    // var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    // return new bootstrap.Tooltip(tooltipTriggerEl)
    // })

    $('.login-form input[type="text"]').addClass('form-control')
    $('.login-form input[type="password"]').addClass('form-control')
    $('.login-form label').addClass('form-label')

    const balloonImgs = [
        'balloon-red.svg',
        'balloon2-red.svg',
        'balloon2-yellow.svg',
        'balloon-yellow.svg',
        'balloon-green.svg',
        'balloon2-green.svg',
    ]
    
    for (let i = 0; i < 30; i++){
        let randomImg = Math.floor(Math.random() * balloonImgs.length)
        // create element
        let balloonImgElement = $(`<img src="/static/images/${balloonImgs[randomImg]}" class="w-20 absolute balloon z-20" />`)

        $('#balloon-container').append(balloonImgElement)
    }


    $('.balloon').each(function() {
        let randomTop = Math.floor(Math.random() * 50)
        let randomRight = Math.floor(Math.random() *100)
        $(this).css({'top': randomTop + 'rem', 'right': randomRight + 'rem'})
    })    

    $('#view-recap').on('click', () => {
        $.ajax({
            url: 'get-recap-id?recap_id=' + recapId,
            method: 'GET',
            // data: JSON.stringify({
            //     'recap_id': recapId
            // }),
            success: function(){
                console.log('SUCCESS!!!')
            },
            error: function(err){
                console.log(err)
            }
        })
    })

//     let scrollAmount = $('.leader-card').outerWidth(true); // Calculate the width of each item including margin
//     setInterval(scrollItems, 3000); // Scroll every 3000ms

//   function scrollItems() {
//     $('#leaders-scroll-area').animate({scrollLeft: "+=" + scrollAmount}, 500);
//   }


})