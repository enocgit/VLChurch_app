$(function(){

    document.documentElement.style.setProperty('--animate-duration', '1.5s');

    $('.edit-btn').css('display', 'none')

        // $('.message-bubble').on('hover', () => {
        //     $('.edit-btn').
        // })

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
})