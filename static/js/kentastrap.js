$(window).scroll(function () {

    // Copas StackOverflow
    let headbtm = $('.kenta-head').height();

    if (isHead && supportBlur) {
        // we round here to reduce a little workload
        stop = Math.round($(window).scrollTop());
        if (stop > headbtm) {
            $('nav')
                .addClass('navbar-light')
                .removeClass('navbar-dark')
                .css({
                    "background-color": "white",
                    "color": "#2F2F2F"
                });
        } else {
            $('nav')
                .addClass('navbar-dark')
                .removeClass('navbar-light')
                .css({
                    "background-color": "rgba(61, 84, 166, 0.2)",
                    "color": "white"
                });
        }
    } else {
        $('nav')
            .addClass('navbar-light')
            .removeClass('navbar-dark')
            .css({
                "background-color": "white",
                "color": "#2F2F2F"
            });
    }

});

$(document).ready(function () {
    $('.kenta-timeline').children().last().find('svg').find('.kenta-timeline-end').remove();

    $('.kenta-timeline-bullet').each(function () {
        var svg = $(this).find('svg');

        if (svg.hasClass('kenta-timeline-past')) {
            svg.attr('fill', '#D9E6EC');
        } else if (svg.hasClass('kenta-timeline-now')) {
            svg.attr('fill', '#ec787c');
        } else {
            svg.attr('fill', '#ffc7b3');
        }
    })

    isHead = $('.kenta-head').length;
    if (!isHead) {
        $('nav')
            .addClass('navbar-light')
            .removeClass('navbar-dark')
            .css({
                "background-color": "white",
                "color": "#2F2F2F"
            });

        $('.kenta-main').children().first().css("margin-top", $("nav").height());
    }

    if (!supportBlur) {
        $('nav')
            .addClass('navbar-light')
            .removeClass('navbar-dark')
            .css({
                "background-color": "white",
                "color": "#2F2F2F"
            });
    }

    $('.kenta-testimonial').click(function () {
        let show = $('.kenta-testimonials-show')
        let img = $(this).find(".kenta-testi-img").css("background-image");
        let name = $(this).find(".kenta-testi-name").html();
        let from = $(this).find(".kenta-testi-from").html();
        let title = $(this).find(".kenta-testi-title").html();
        let text = $(this).find(".kenta-testi-text").html();
        show.find(".kenta-testi-img").css("background-image", img);
        show.find(".kenta-testi-name").html(name);
        show.find(".kenta-testi-from").html(from);
        show.find(".kenta-testi-title").html(title);
        show.find(".kenta-testi-text").html(text);
    });

});

let isHead = true;
let supportBlur = CSS.supports("backdrop-filter", "blur(100px)");
