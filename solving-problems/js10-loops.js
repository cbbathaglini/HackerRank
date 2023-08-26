function vowelsAndConsonants(s) {
    var arr_vogais = ['a','e','i','o','u']
    var arr_consoantes = []
    var i = 0
    for(i=0; i<= s.length; i++){
       if(arr_vogais.includes(s[i])){
           console.log(s[i])
       }else{
           arr_consoantes.push(s[i])
       }  
    }
    console.log(arr_consoantes.join('\n'));
        
}