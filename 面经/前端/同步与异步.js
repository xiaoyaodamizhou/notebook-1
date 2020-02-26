const fs = require('fs')

const log = console.log.bind(console)

/*
* 同步和异步编程的概念
*
* 同步的意思是 函数通过返回值来传递数据
* 函数从获取数据一直到返回数据之间的时间一直在等待
*
* 异步的意思是 函数通过回调函数的方式来传递获取的数据
* 函数执行后立刻就返回了，数据获取成功后，调用回调函数并传递参数
* */

// 我们先写入一个文件
// 写入成功后, 读取当前目录看是否有这个文件
// 如果有这个文件，我们读取文件的内容并且打印出来
// 然后我们删除这个文件

let file = 'message.txt'
let s = 'hello node.js'

// log('写入前')
//
// fs.writeFile(file, s, (error) => {
//     if (error !== null) {
//         // 没有写入成功
//     } else {
//         log('写入成功')
//         fs.readdir('.', (error, files) => {
//             if (files.includes(file)) {
//                 fs.readFile(file, (error, data) => {
//                     // data 不是一个字符串, 而是一个 buffer(二进制数组)
//                     log('读取文件内容', data.toString())
//                     fs.unlink(file, (error) => {
//                         log('删除文件成功')
//                     })
//                 })
//             }
//         })
//     }
// })
//
// log('写入后')

// console.time 和 console.timeEnd 是用来测程序执行时间的
// 要求这两个函数的参数完全一致

const processFile = () => {
    log('同步写入前')

    for (let i = 0; i < 1000; i++) {
        fs.writeFileSync(file, s)
    }
    log('写入成功')
    let files = fs.readdirSync('.')
    if (files.includes(file)) {
        let data = fs.readFileSync(file)
        log('读取文件内容', data)
        fs.unlinkSync(file)
        log('删除文件成功')
    }

    log('同步写入后')
}

const guasync = (func) => {
    // 第二个参数的意思是延迟 x ms 执行程序
    // 延迟的意思是排队, 就是说延迟 x ms 把这个函数放到队伍里
    setTimeout(() => {
        func()
    }, 0)
}

console.time('sync')
log('sync 开始执行 1')
processFile()
log('sync 开始执行 2')
console.timeEnd('sync')


console.time('guasync')
log('guasync 开始执行 1')
guasync(processFile)
log('guasync 开始执行 2')
console.timeEnd('guasync')

