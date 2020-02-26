var log = function () {
    console.log(arguments)
};

var commentTemplate = function (comments) {
    var c = comments;
    var t = `
      <div class="comment-cell cell item">
            <div>
                <span>${ c.comment }</span>
                <span class="right span-margin">${ c.user.username }</span>
                <span class="right span-margin">${ c.created_time }</span>
                    <span class="right span-margin">
                        <img src="${ c.user.avatar }" class="avatar">
                    </span>
            </div>
        </div>
        <div class="right span-margin">
            <button class="comment-delete" data-id="${ c.id }">删除</button>
            <a href="#" class="com">评论</a>
         </div>
    `
    return t
};


var bindEventCommentHide = function () {
    $('a.com').on('click', function () {
        $(this).parent().next().slideToggle();
        return false;
    });
};

//绑定删除事件，并进行事件委托，通过静态的.weibo-container进行委托
var bindEventCommentDelete = function () {
    $('.topic-comment-container').on('click', '.comment-delete', function () {
        var commentId = $(this).data('id');
        //log('comment_id', commentId)
        var commentCell = $(this).closest('.comment-cell');
        var line_straight = $(this).closest('.line-straight');
        log('line_straight', $(line_straight).text());

        var success = function (response) {
            log('删除成功', arguments);
            //动态的删除
            $(commentCell).slideUp();
            $(document).remove($(line_straight));
        };
        var error = function () {
            log('删除失败', arguments);
        };
        api.commentDelete(commentId, success, error)
    });
};

var bindEventCommentAdd = function () {
    $('.topic-comment-container').on('click', '.id-button-comment-add', function () {
        var comment = $('.id-input-comment').val();
        var topic_id = $('.topic-id').attr('id');
        log('topic_id', topic_id);
        var form = {
            comment: comment,
            topic_id: topic_id
        };
        var response = function (r) {
            log('成功', arguments);
            log('response', r);
            log('data', r.data);
            if (r.success) {
                var w = r.data;
                log('w type', w);
                var topic_id = r['topic_id'];
                var topics = $('topic-comment-container');
                var topic = document.getElementById(topic_id);
                //log('topic', to pic);
                topic = $(topic);
                topic.prepend(commentTemplate(w));
                //$('.comment-container').prepend(commentTemplate(w));
            } else {
                log('添加失败');
                alert(r.message)
            }
        };
        api.commentAdd(form, response)
    });
};

var bindEvents = function () {
    bindEventCommentHide();
    bindEventCommentAdd();
    bindEventCommentDelete();
};

$(document).ready(function () {
    bindEvents();
});