HTML 部分
localStorage 和 cookies
// localStorage、 sessionStorage 与 cookies 的区别

FormData
// 上传文件需要用到这个对象
// 将数据变成键值对的形势

File API
// 预览图片使用



CSS 部分
float
position
display
两栏布局
水平居中
垂直居中

两栏布局：
float, postion, overflow, table, 



JS 部分
值类型与引用类型
//
var a = {
    v: 1
}
var b = a
console.log(b.v)

a.v = 2
console.log(b.v)

a = {
    v: 3
}
console.log(b.v)




// 变量声明提升
// 这段代码
console.log(a)
var a = 1
// 相当于
var a
console.log(a)
a = 1


// 这段代码
console.log(b())
function b() {
    return 2
}
// 相当于
var b = function() {
    return 2
}
console.log(b())


// 这段代码
console.log(c())
var c = function() {
    return 3
}
// 相当于
var c
console.log(c())
c = function() {
    return 3
}

// 注意，let 或者 const 声明的变量不具备声明提升的特性
console.log(d)
let d = 4




// this
//
var x = 0
function test() {
    console.log(this.x)
}
var o = {}
o.x = 1
o.m = test
o.m()
o['m']()
o.m.apply()


// this + arguments
var gua = 'name 001'
var foo = function(){
    console.log(arguments['0']())
    // console.log(arguments[0]())
}

var o = {}
o.gua = 'name 000'
o.func = foo
o.func(function(){
    return this.gua
})

o.func2 = function(){
    arguments.gua = 'gua'
    console.log(arguments[0]())
}

o.func2(function(){
    return this.gua
})


// prototype
// 原型链
//
function Foo() {
    this.name = 'a'
}

var f1 = new Foo()
f1.name = 'b'
console.log(f1.name)

var f2 = new Foo()
console.log(f2.name)



arguments
//
(function() {
    return typeof arguments
})()
(function() {
    console.log(arguments)
})(1, 2, 3)

(function(...args) {
    console.log(args)
})(1, 2, 3)



call, apply, bind
// call, apply 和 bind 的区别

setTimeout 和 setInterval
// 两者的区别

setTimeout 与循环结合
//
for (var i = 0; i < 5; i++) {
    setTimeout(function() {
        console.log(new Date(), i)
    }, 1000)
}
console.log(new Date(), i)

for (var i = 0; i < 5; i++) {
    setTimeout(function() {
        console.log(new Date(), i)
    }, 0)
}

for (let i = 0; i < 5; i++) {
    setTimeout(function() {
        console.log(new Date(), i)
    }, 0)
}

let i = 0
for (; i < 5; i++) {
    setTimeout(function() {
        console.log(new Date(), i)
    }, 0)
}



事件冒泡, 事件捕获, 事件委托
// 讲清楚这三个概念

闭包
// 所谓经典的闭包面试题(上课讲)
// 使用闭包实现如下程序
// 函数每调用一次，该函数的返回值加 1
/*
本来foo调用完i应该被销毁，但因为返回的函数引用了i,所以i被记住了
*/
var foo = function(){
    var i = 0
    return function(){
        i++
        return i
    }
}
var a = foo()
a()
a()

clone 和 deepClone
// 实现 clone 和 deepClone 函数
// clone栈内存中新建一个变量，就是指针，但是都指向同一个堆内存的数据。本质就是一个对象
// 深克隆，复制值一样，但是本质不是一样的东西。一般使用JSON实现该功能
const deepClone1 = obj => {
    var _tmp, result
    _tmp = JSON.stringify(obj)
    result = JSON.parse(_tmp)
    return result
}


ajax（可能需要手写原生的 ajax）
// 实现原生的 ajax 函数
// readyState 0 1 2 3 4 各代表什么含义



HTTP 请求方法, 常见状态码, 头部常见字段
// HTTP 有哪些常见请求方法 GET POST PUT PATCH DELETE
// HTTP 常见状态码有哪些 200 301 302 403 404 500 502
// HTTP 头部常见字段有哪些
    Content-Type
    Content-Length


跨域 （jsonp, postMessage, cors, 用服务器(比如 node)转发请求和响应）
// 跨域有哪些常见的解决方式

网络安全: xss, csrf
// xss 和 csrf 的原理是什么

DOM 操作（查找, 添加, 删除, 修改）
// DOM 查找/添加/删除/修改对应的 API 是什么

jQuery 常见 API
// jQuery 常见 API




数据结构
数组
对象
队列
栈
数组、对象、字符串的想换转化
比如 a=1&b=2&c=3 怎样转成对象, 复习基础课程的作业就可以
// 有这样一个 url： http://vip.qq.com/a.java?a=1&b=2&c=3&d=xxx&e
// 写一段 JS 程序将 url 的参数转成对象的形式
{
    a: 1,
    b: 2,
    c: 3,
    d: 'xxx',
    e: '',
}




ES6
ES6 的面试题一般是概念性质的, 所以清楚下面的概念就可以了
let 和 const, 有一个 TDZ（暂时性死区的概念，了解下即可）
箭头函数
解构
剩余参数
Promise, 可能会附带 async await
class
Set

// 用解构来简化参数列表
var gua = function({name, height}) {
    console.log(name, height)
}
var gua2 = function(info) {
    console.log(info.name, info.height)
}

var info = {
    name: 'gua',
    height: 169,
}

gua(info)


React
// React 也是概念性质的题目为主, 基本上不会考察写代码
React Angular 这 2 个一般只会一个就可以的, 所以这里只说 React 的情况
react 的广告
virtual dom
diff 算法的原理
state 和 props
组件生命周期
组件通信：父组件 -> 子组件, 子组件 -> 父组件, A 组件 -> B 组件
React Router（react 路由）
Redux/MobX
react ui 有两套很流行: Material UI 和 Ant Design, 国内流行的是 Ant Design
