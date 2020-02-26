export function saveToLocal(id, key, value) {
  let seller = window.localStorage.__seller__
  if (!seller) {
    seller = {}
    seller[id] = {}
  } else {
    seller = JSON.parse(seller)
    if (!seller[id]) {
      seller[id] = {}
    }
  }
  seller[id][key] = value
  window.localStorage.__seller__ = JSON.stringify(seller)
}

export function loadFromLocal(id, key, def) {
  let sellers = JSON.parse(window.localStorage.__seller__)
  if (!sellers) {
    return def
  }
  let seller = sellers[id]
  if (seller) {
     return seller[key]
  } else {
    return def
  }
}
