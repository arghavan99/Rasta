$(window).scroll(function(event) {
    let scroll = $(window).scrollTop();
    if (scroll > 20) {
        $(".r-nav").addClass("active-nav");
    } else {
        $(".r-nav").removeClass("active-nav");
    }
});

