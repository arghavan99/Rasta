
$(window).load(function () {
$('.special.cards .image').dimmer({
  on: 'hover'
});
});

$(window).resize(toggle);
$(window).load(toggle);


function toggle () {
      var parentwidth = $(".parent").width();
      $('.child').css('max-width', parentwidth+"px");
  }