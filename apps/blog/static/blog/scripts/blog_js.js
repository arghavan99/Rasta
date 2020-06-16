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

$(document).on('submit', '#comment_form', function (e) {
        e.preventDefault();
        var form = document.getElementById('comment_form');
        $.ajax(
            {type: 'POST',
            url: '/blog/submit_c_r/',
            data: $(form).serialize(),
            dataType: 'json',
            success: function (res) {
                if (res.bibot_err == 'error') {
                    $('#cm_form_err')[0].innerHTML = '<li class="error">احراز هویت ناموق</li>';
                    return;
                }
                BibotCaptcha.reload_bibot('bibot-captcha');
                $("#comment_form")[0].reset();
                $('#cm_form_err')[0].innerHTML = '';
                $('#all_comments').append('<div class="comment" id="cm_' + res.comment.id + '">' +
                                          '<a class="avatar"><svg id="cm_' + res.comment.id +'_svg"></svg></a>' +
                                          '<div class="content">' +
                                          '<a class="author">' + res.comment.author_name + '</a>' +
                                          '<div class="metadata">' +
                                          '<div class="date">' + res.comment.date_time+ '</div>' +
                                          '</div>' +
                                          '<div class="text">' + res.comment.text + '</div>' +
                                          '<div class="actions">' +
                                          '<a class="reply" id="reply_button_' + res.comment.id +
                                          '" onclick="create_reply_form(' + res.comment.id + ')">پاسخ</a>' +
                                          '</div>'+
                                          '<div class="comments" id="replies_' + res.comment.id + '"></div>' +
                                          '</div></div>');
                jdenticon.update('#cm_' + res.comment.id + '_svg', res.comment.author_name);
                }
           }
        )
    })


function submit_reply(comment_id) {
    var form = $('#reply_form_' + comment_id);
    $.ajax(
            {type: 'POST',
            url: '/blog/submit_c_r/',
            data: $(form).serialize(),
            dataType: 'json',
            success: function (res) {
                if (res.bibot_err == 'error') {
                    if ($('#reply_form_err'))
                        $('#reply_form_err')[0].innerHTML = '<li class="error">احراز هویت ناموق</li>';
                    return;
                }
                $('#reply_form_div' + comment_id).remove();
                remove_form = -1;
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
                document.getElementById('reply_button_' + comment_id).innerText = "پاسخ";
                }
           }
        )
}

function remove_prev_form(comment_id) {
    if(comment_id!=remove_form && remove_form != -1) {
        var junk = document.getElementById('reply_form_div'+remove_form);
        junk.parentElement.removeChild(junk);
        if(document.getElementById('reply_button_'+remove_form).innerText =="لغو پاسخ")
            document.getElementById('reply_button_'+remove_form).innerText = "پاسخ";
    }
}

var remove_form = -1;

function create_reply_form(comment_id) {
    var x = document.getElementById('reply_form_div'+comment_id);
    remove_prev_form(comment_id);
    if(x!= null) {
        if(document.getElementById('reply_button_'+comment_id).innerText =="لغو پاسخ")
            document.getElementById('reply_button_'+comment_id).innerText = "پاسخ";

        x.parentElement.removeChild(x);
        remove_form = -1
    } else {
        document.getElementById('reply_button_'+comment_id).innerText= "لغو پاسخ";
        var reply_form = document.createElement('div');
        reply_form.id = 'reply_form_div' + comment_id;
        reply_form.class = 'ui stackable grid';
        reply_form.innerHTML = get_form_template(comment_id);

        remove_form = comment_id;
        document.getElementById('cm_' + comment_id).appendChild(reply_form);
        BibotCaptcha.reload_bibots();
    }

    $(document).on('submit', '#reply_form_' + comment_id, function (e) {
        e.preventDefault();
        submit_reply(comment_id);})
}