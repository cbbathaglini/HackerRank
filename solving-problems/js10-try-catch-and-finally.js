function reverseString(s) {
    try{
        s = s.split("").reverse().join("");   
    }catch({ name, message }){
        console.log(message)    
    }
    console.log(s)
   
}