function permutationEquation(p) {
    var arr_final = []
    var i =0
    for(i=0; i<p.length;i++){
        arr_final.push(p.indexOf(p.indexOf(i+1)+1)+1);
    }
    return arr_final;

}