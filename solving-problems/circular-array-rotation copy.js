function circularArrayRotation(a, k, queries) {
    var n = a.length
    var arr_aux = []
    var i =0
    for( i=0; i<k;i++){
        a.unshift(a[n-1])
        a.pop()
    }
        
    for( i=0; i<queries.length;i++){
        arr_aux.push(a[queries[i]])
    }
    return arr_aux

}