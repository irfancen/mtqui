$(window).scroll(function () {

    // Copas StackOverflow
    var headbtm = $('.kenta-head').height();

    // we round here to reduce a little workload
    stop = Math.round($(window).scrollTop());
    if (stop > headbtm) {
        $('nav')
            .addClass('navbar-light')
            .removeClass('navbar-dark')
            .css({
                "background-color": "white",
                "color" : "#2F2F2F"
            });
    } else {
        $('nav')
            .addClass('navbar-dark')
            .removeClass('navbar-light')
            .css({
                "background-color": "rgba(61, 84, 166, 0.2)",
                "color" : "white"
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
            svg.attr('fill', '#FFB3B6');
        } else {
            svg.attr('fill', '#FFD7D3');
        }
    })
});

