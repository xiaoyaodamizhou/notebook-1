var api = {};

var log = function(){
  console.log(arguments);
};

api.ajax = function(url, method, form, error, success){
    var request = {
        url: url,
        type: method,
        data: form,
        success: function(response){
            log('response', response);
            var r = JSON.parse(response);
            log('response parse', r);
            success(r)
        },
        error: function(){
            log('网络错误', error);
            var r = {
                'success': false,
                 message: '网络错误'
            };
            error(r)
        }
    };
    log('request url', request.url);
    $.ajax(request);
};

api.get = function(url, success, error){
    log('url get', url);
    api.ajax(url, 'get', {}, success, error)
};

api.post = function(url, form, response){
    api.ajax(url, 'post', form, response, response)
};

api.commentAdd = function(form, response){
    var url = '/api/comment/add';
    api.post(url, form, response)
};

api.commentDelete = function(commentId, success, error){
    var url = 'api/comment/delete/' + commentId;
    api.get(url, success, error)
};
