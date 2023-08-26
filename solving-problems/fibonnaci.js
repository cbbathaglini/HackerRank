function fibonnaci(n){
    if( n <= 1 && n >=0){
        return n
    }

    return fibonnaci(n-1) + fibonnaci(n-2)
}



test('fibonacci deve retornar 2 para o valor 3', ()=>{
    expect(fibonnaci(3)).toEqual(2);
})