$(window).load(function () {
$('.special.cards .image').dimmer({
  on: 'hover'
});
});


$(window).scroll(function () {
    if ($(window).width() >= 768) {
        if ( $(window).scrollTop() >= 100 ) {
            $('.child').css('top', "15%");
        } else {
            $('.child').css('top', "30%");
        }
    }
});


function toggle () {
    var parentwidth = $(".parent").width();
    $('.child').css('max-width', parentwidth+"px");
}


$(window).resize(toggle);
$(window).load(toggle);