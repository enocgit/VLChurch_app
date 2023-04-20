$(function(){

    document.documentElement.style.setProperty('--animate-duration', '1.5s');


    $(window).on({
        scroll: function(){
            let scrollTop = $(window).scrollTop()
            // if (scrollTop > 200){
            //     $('#about .vision .pic').css({'visibility': 'visible'})
            //     $('#about .vision .pic').css({'transition': '1s all ease-in-out'})
            //     $('#about .vision .inside-pic').css({'visibility': 'visible'})
            //     $('#about .vision .inside-pic').addClass('animate__animated animate__fadeInLeft')
            //     // $('#about .vision .inside-pic').css({'visibility': 'visible'})
            //     // $('#about .vision .inside-pic').addClass('animate__animated animate__fadeInTop')
            // }
            if (scrollTop >120) {
                $('#brand-sub').removeClass('invisible')
                $('#brand-sub').addClass('visible')
                $('#brand-sub').fadeIn()
            }
            if (scrollTop < 120){
                $('#brand-sub').addClass('invisible')
            }
            // if (scrollTop > 400){
                // fellowship
                // $('#men-fellow .square').css({'visibility': 'visible'})
                // $('#men-fellow .square').addClass('animate__animated animate__fadeIn')
            //     // location
                // $('#home-location .p').css({'visibility': 'visible'})
                // $('#home-location .h1').css({'visibility': 'visible'})
                // $('#home-location .btn-help').css({'visibility': 'visible'})
                // $('#home-location p').removeClass('invisible')
                // $('#home-location p').addClass('visible')
                // $('#home-location p').addClass('animate__animated animate__fadeInRight')
                // $('#home-location h2').removeClass('invisible')
                // $('#home-location h2').addClass('visible')
                // $('#home-location h2').addClass('animate__animated animate__fadeInLeft')

                // $('#home-location .btn-help').addClass('animate__animated animate__fadeInLeft')
                // alert('hi')
            //     // prompt('100')
            // }
    //         if (scrollTop > 500){
    //             $('#about-vision .left-content').removeClass('invisible')
    //             $('#about-vision .left-content').addClass('visible')
    //             $('#about-vision .left-content').addClass('animate__animated animate__fadeInLeft')
                
    //             $('#about-vision .right-content h2').removeClass('invisible')
    //             $('#about-vision .right-content h2').addClass('visible')
    //             $('#about-vision .right-content h2').addClass('animate__animated animate__fadeInDown') 
                
    //             $('#about-vision .right-content p').removeClass('invisible')
    //             $('#about-vision .right-content p').addClass('visible')
    //             $('#about-vision .right-content p').addClass('animate__animated animate__fadeInLeft')
    //             $('#men-fellow div').removeClass('invisible')
    //             $('#men-fellow div').addClass('visible')
    //             $('#men-fellow div').addClass('animate__animated animate__fadeIn')
    //         }
    //         if (scrollTop > 800){
    //         }
        
    //         if (scrollTop > 900){
    //             $('#home-giving p').removeClass('invisible')
    //             $('#home-giving p').addClass('visible')
    //             $('#home-giving p').addClass('animate__animated animate__fadeInLeft')
    //             $('#home-giving h2').removeClass('invisible')
    //             $('#home-giving h2').addClass('visible')
    //             $('#home-giving h2').addClass('animate__animated animate__fadeInLeft')

    //             $('#home-giving button').removeClass('invisible')
    //             $('#home-giving button').addClass('visible')
    //             $('#home-giving button').addClass('animate__animated animate__fadeInDown')

    //             $('#home-giving img').removeClass('invisible')
    //             $('#home-giving img').addClass('visible')
    //             $('#home-giving img').addClass('animate__animated animate__fadeInRight')
                
    //         }
    //         if(scrollTop > 1000){
    //         }
    //         if (scrollTop > 1200){
    //             // women fellowship
    //             $('#women-fellow h1').removeClass('invisible')
    //             $('#women-fellow h1').addClass('visible')
    //             $('#women-fellow h1').addClass('animate__animated animate__flipInX')
    //         }
    //         if (scrollTop > 1400){
    //             $('#home-prayer .right-content').removeClass('invisible')
    //             $('#home-prayer .right-content').addClass('visible')
    //             $('#home-prayer .right-content').addClass('animate__animated animate__fadeInUp')
    //             $('#home-prayer .left-content').removeClass('invisible')
    //             $('#home-prayer .left-content').addClass('visible')
    //             $('#home-prayer .left-content').addClass('animate__animated animate__fadeInLeft')
                
    //         } if (scrollTop > 1900){
    //             $('#home-leaders .leader-card').removeClass('invisible')
    //             $('#home-leaders .leader-card').addClass('visible')
    //             $('#home-leaders .leader-card').removeClass('invisible')
    //             $('#home-leaders .leader-card').addClass('visible')
    //             $('#home-leaders .leader-card').addClass('animate__animated animate__fadeInUp')
    //             $('#home-leaders h2').removeClass('invisible')
    //             $('#home-leaders h2').addClass('visible')
    //             $('#home-leaders h2').addClass('animate__animated animate__fadeInDown')
                
    //         }
    //         // if (scrollTop > 700){
    //         //     $('.main-leaders .row').css({'visibility': 'visible'})
    //         //     $('.main-leaders .head').css({'visibility': 'visible'})
    //         //     $('.main-leaders .row').addClass('animate__animated animate__fadeIn')
    //         //     $('.main-leaders .head').addClass('animate__animated animate__fadeIn')
    //         //     // prompt('100')
    //         // }
    //         // if (scrollTop > 1180){
    //         //     // women fellowship
    //         //     $('.main-footer').css({'visibility': 'visible', 'transition': 'all 0.5s ease-in-out'})
    //         //     $('.main-footer').addClass('animate__animated animate__fadeInTop')
    //         // }

        }
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
    
    // var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    // var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    // return new bootstrap.Tooltip(tooltipTriggerEl)
    // })

    $('.login-form input[type="text"]').addClass('form-control')
    $('.login-form input[type="password"]').addClass('form-control')
    $('.login-form label').addClass('form-label')


})