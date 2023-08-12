
def find_position(letra):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    return alphabet.index(letra)

def designerPdfViewer(h, word):
    heights = []
    num_letters = len(word)
    for i in range(num_letters):
        position = find_position(word[i])
        heights.append(h[position])
                
    return num_letters * max(heights) 