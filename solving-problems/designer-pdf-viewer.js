function find_position(letter){
    var alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    return alphabet.indexOf(letter)
}


function designerPdfViewer(h, word) {
    var i =0, position = 0
    var array_heights = []
    for(i=0; i<word.length; i++){
        position = find_position(word[i])
        array_heights.push(h[position])
    }

    return array_heights.sort().reverse()[0] * word.length

}