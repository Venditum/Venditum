let r = [[true, false, false], [false, false]]
function enthälttrue(DArray){
    return DArray.some(zeile => zeile.includes(true))
}

alert(enthälttrue(r))