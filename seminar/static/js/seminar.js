$(window).scroll(function () {

    // Copas StackOverflow
    var headbtm = $('.carousel').height();

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