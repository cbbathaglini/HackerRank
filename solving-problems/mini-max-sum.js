function miniMaxSum(arr) {
    arr.sort()
    console.log(soma_array(arr,0,4)+" "+soma_array(arr,1,5))

}

function soma_array(arr, inicio, final){
    var i =0, soma = 0
    for(i=inicio; i<final;i++){
        soma += arr[i]
    }
    return soma
}