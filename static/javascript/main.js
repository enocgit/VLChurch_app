$(function(){

    document.documentElement.style.setProperty('--animate-duration', '1.5s');


    $(window).on({
        scroll: function(){
            let scrollTop = $(window).scrollTop()
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