var ajax = function(method, url, data, runCallBack){
    var r = new XMLHttpRequest()
    r.open(method, url, true)
    r.setRequestHeader('Content-Type', 'application/json')
    r.onreadystatechange = function(){
        if(r.readyState == 4){
            runCallBack(r.response)
        }
    }
    r.send(data)
}

var log = function(){
    console.log.apply(console, arguments)
}

var template = function(data){
    var passage = `
        <div class="todo-cell row">
                <div class="todo-content col-sm-8 col-md-8 col-lg-8 col-xs-8">
                    <span class="col-sm-3 col-md-3 col-lg-3 col-xs-3">${data.id}</span>
                    <span class="col-sm-3 col-md-3 col-lg-3 col-xs-3">${data.task}</span>
                    <span class="col-sm-3 col-md-3 col-lg-3 col-xs-3">${data.time}</span>
                    <span class="col-sm-3 col-md-3 col-lg-3 col-xs-3">${data.done}</span>
                </div>
                <div class="todo-edit col-sm-4 col-md-4 col-lg-4 col-xs-8">
                    <button class="btn btn-success btn-sm todo-done">done</button>
                    <button class="btn btn-success btn-sm todo-update">update</button>
                    <button class="btn btn-success btn-sm todo-delete">delete</button>
                </div>
        </div>
    `
    return passage
}

var appendHtml = function(selector, template){
    selector.insertAdjacentHTML('beforeend', template)
}

var AddEvent = function(){
    var todo_input = document.querySelector('.todo-input')
    var url = '/api/todo/add'
    var task = document.querySelector('input[type="text"]').value
    var t = {
        'task': task,
    }
    var message = JSON.stringify(t)
    log('post message add', message)
    var Add_runCallBack = function(data){
       var dt = JSON.parse(data)
        if(dt.success){
            var t = dt.data
            t = JSON.parse(t)
            var todo_box = document.querySelector('.todo-box')
            appendHtml(todo_box, template(t))
        }else{
            log('error', dt.message)
        }
    }
    ajax('POST', url, message, Add_runCallBack)
}

var toggleClass = function(element, className){
    if(element.classList.contains(className)){
        element.classList.remove(className)
    }else{
        element.classList.add(className)
    }
}

var UpdateEvent = function(target){
    //var url = '/api/todo/update'
    //var id = target.parentElement().dataset.id
    //var todos = document.querySelectorAll('.todo-cell')
    //var todo_cell = {
    //    'task': '',
    //    'done': false
    //}
    //for(var i = 0; i < todos.length; i++){
    //    var todo = todos[i]
    //    var span = todo.querySelectorAll('span')[0]
    //    var ID = span.text
    //    if(id == ID){
    //        toggleClass(todo, 'edit')
    //        var spans = todo.querySelectorAll('.todo-cell')
    //        if(todo.classList.contains('edit')){
    //            for(var s of spans){
    //                s.contenteditable = true
    //            }
    //        }
    //    }
    //
    //}
    //var Add_runCallBack = function(data){
    //   var dt = JSON.parse(data)
    //    if(dt.success){
    //        var t = dt.data
    //        t = JSON.parse(t)
    //        var todo_box = document.querySelector('.todo-box')
    //        appendHtml(todo_box, template(t))
    //    }else{
    //        log('error', dt.message)
    //    }
    //}
    //ajax('POST', url, message, Add_runCallBack)
}

var DeleteEvent = function(){}

var update = function(){
    var update_button = document.querySelector('.input-update')
    log('update_button', update_button)
    update_button.addEventListener('click', function(event){
        var target = event.target
        UpdateEvent(target)
    })
}

var add = function(){
    var add_button = document.querySelector('.input-add')
    log('add_button', add_button)
    add_button.addEventListener('click', function(){
        AddEvent()
    })
}

var main = function(){
   add()
}

window.onload = function () {
    main()
}