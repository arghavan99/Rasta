$(window).load(function () {
    $('.ui.dropdown')
        .dropdown()
    ;
    $('.ui.accordion')
        .accordion()
    ;
    $('.special.cards .image').dimmer({
  on: 'hover'
});
});

function create_reply_form(comment_id) {
    var reply_form = document.createElement('div');
    reply_form.class = 'ui stackable grid';
//    reply_form.innerHTML = '<p>hii</p>';
    reply_form.innerHTML = '<form id="blog_form" method="post" class="ui form error" style="margin:auto;width: 90%"><input type="text" name="author_name"></form>'
    document.getElementById('cm_' + comment_id).appendChild(reply_form);
}