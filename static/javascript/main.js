// // Set a timeout to hide the navbar after the user stops scrolling
// let timeout;

// // Listen for the scroll event on the window object
// window.addEventListener('scroll', function() {
//   // Show the navbar
//   document.querySelector('.navbar').style.display = 'block';

//   // Clear the timeout if it has been set
//   if (timeout) {
//     clearTimeout(timeout);
//   }

//   // Set a new timeout to hide the navbar after 1 second
//   timeout = setTimeout(function() {
//     document.querySelector('.navbar').style.display = 'none';
//   }, 1000);
// });

$(document).ready(function(){
    $(window).scroll(() => {
        let scrollTop = $(window).scrollTop()
        if (scrollTop > 200){
            $('#about .vision .pic').css({'visibility': 'visible'})
            $('#about .vision .pic').css({'transition': '1s all ease-in-out'})
            $('#about .vision .inside-pic').css({'visibility': 'visible'})
            $('#about .vision .inside-pic').addClass('animate__animated animate__fadeInLeft')
            // $('#about .vision .inside-pic').css({'visibility': 'visible'})
            // $('#about .vision .inside-pic').addClass('animate__animated animate__fadeInTop')
        }
        if (scrollTop > 400){
            // fellowship
            $('#men-fellow .square').css({'visibility': 'visible'})
            $('#men-fellow .square').addClass('animate__animated animate__fadeIn')
            // location
            $('.main-location .lead').css({'visibility': 'visible'})
            $('.main-location .head').css({'visibility': 'visible'})
            $('.main-location .btn-help').css({'visibility': 'visible'})
            $('.main-location .lead').addClass('animate__animated animate__fadeInRight')
            $('.main-location .head').addClass('animate__animated animate__fadeIn')
            $('.main-location .btn-help').addClass('animate__animated animate__fadeInLeft')
            // prompt('100')
        }
        if (scrollTop > 700){
            $('.main-leaders .row').css({'visibility': 'visible'})
            $('.main-leaders .head').css({'visibility': 'visible'})
            $('.main-leaders .row').addClass('animate__animated animate__fadeIn')
            $('.main-leaders .head').addClass('animate__animated animate__fadeIn')
            // prompt('100')
        }
        if (scrollTop > 1100){
            // women fellowship
            $('#women-fellow h1').css({'visibility': 'visible'})
            $('#women-fellow h1').addClass('animate__animated animate__flipInX')
        }
        // if (scrollTop > 1180){
        //     // women fellowship
        //     $('.main-footer').css({'visibility': 'visible', 'transition': 'all 0.5s ease-in-out'})
        //     $('.main-footer').addClass('animate__animated animate__fadeInTop')
        // }
    })

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
    
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
    })

    $('.login-form input[type="text"]').addClass('form-control')
    $('.login-form input[type="password"]').addClass('form-control')
    $('.login-form label').addClass('form-label')


})