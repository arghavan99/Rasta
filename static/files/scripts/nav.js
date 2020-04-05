$(window).scroll(function(event) {
    let scroll = $(window).scrollTop();
    if (scroll > 10) {
        $(".r-nav").addClass("active-nav");
    } else {
        $(".r-nav").removeClass("active-nav");
    }
});

