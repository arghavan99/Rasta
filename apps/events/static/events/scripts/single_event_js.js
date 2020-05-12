$(window).load(function () {
$('.special.cards .image').dimmer({
  on: 'hover'
});
});

var distance = 100;

$(window).scroll(function () {
    if ($(window).width() >= 768) {
        if ( $(window).scrollTop() >= distance ) {
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