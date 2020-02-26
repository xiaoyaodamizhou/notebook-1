// 解析出url的query
export function urlParse() {
  let url = window.location
  let search = url.search
  let obj = {}
  let reg = /[?&][^?&]+=[^?&]+/g
  let arr = search.match(reg)
  if (arr) {
    arr.forEach((item) => {
      item = decodeURIComponent(item)
      let tempArr = item.substring(1).split('=')
      let [k, v] = tempArr
      obj[k] = v
    })
  }
  return obj
}
