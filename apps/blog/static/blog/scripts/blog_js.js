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

$(document).on('submit', '#comment_form', function (e) {
        e.preventDefault();
        var form = document.getElementById('comment_form');
        $.ajax(
            {type: 'POST',
            url: '/blog/submit_c_r/',
            data: $(form).serialize(),
            dataType: 'json',
            success: function (res) {
                if (res.bibot_err == 'error')
                    return;
                $("#comment_form")[0].reset();
                $('#all_comments').append('<div class="comment" id="cm_' + res.comment.id + '">' +
                                          '<a class="avatar"><svg id="cm_' + res.comment.id +'_svg"></svg></a>' +
                                          '<div class="content">' +
                                          '<a class="author">' + res.comment.author_name + '</a>' +
                                          '<div class="metadata">' +
                                          '<div class="date">' + res.comment.date_time+ '</div>' +
                                          '</div>' +
                                          '<div class="text">' + res.comment.text + '</div>' +
                                          '<div class="actions">' +
                                          '<a class="reply" onclick="create_reply_form(' + res.comment.id + ')">Reply</a>' +
                                          '<div class="comments" id="replies_"' + res.comment.id + '></div>' +
                                          '</div></div></div>');
                jdenticon.update('#cm_' + res.comment.id + '_svg', res.comment.author_name);
                }
           }
        )
    })


function submit_reply(comment_id) {
    var form = $('#reply_form_' + comment_id);
    console.log($(form))
    $.ajax(
            {type: 'POST',
            url: '/blog/submit_c_r/',
            data: $(form).serialize(),
            dataType: 'json',
            success: function (res) {
                if (res.bibot_err == 'error')
                    return;
                form.remove();
                $('#replies_' + comment_id).append('<div class="comment" id="reply_' + res.reply.id + '">' +
                                          '<a class="avatar"><svg id="reply_' + res.reply.id +'_svg"></svg></a>' +
                                          '<div class="content">' +
                                          '<a class="author">' + res.reply.author_name + '</a>' +
                                          '<div class="metadata">' +
                                          '<div class="date">' + res.reply.date_time+ '</div>' +
                                          '</div>' +
                                          '<div class="text">' + res.reply.text + '</div>' +
                                          '</div></div></div>');
                jdenticon.update('#reply_' + res.reply.id + '_svg', res.reply.author_name);
                $('#reply_button_' + comment_id).show();
                }
           }
        )
}