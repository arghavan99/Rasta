
$(window).load(function () {
$('.special.cards .image').dimmer({
  on: 'hover'
});
});
$(window).resize(toggle);
$(window).load(toggle);
var distance = 100;

$(window).scroll(function () {
 if ( $(window).scrollTop() >= distance ) {
        $('.child').css('top', "10%");}
});
$(window).scroll(function () {
 if ( $(window).scrollTop() <= distance ) {
        $('.child').css('top', "30%");}
});

function toggle () {
      var parentwidth = $(".parent").width();
      $('.child').css('max-width', parentwidth+"px");
  }







