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
        if (scrollTop > 400){
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
    })
})